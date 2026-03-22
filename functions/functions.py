import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cft 
from datetime import datetime, timedelta




def load_index():
    try:
        df_index = pd.read_csv('https://data-argo.ifremer.fr/argo_synthetic-profile_index.txt',
                               skiprows = 8,
                               usecols = ['file', 'date', 'latitude', 'longitude', 'parameters']
                              )
    except:
        df_index = pd.read_csv('https://usgodae.org/pub/outgoing/argo/argo_synthetic-profile_index.txt',
                               skiprows = 8,
                               usecols = ['file', 'date', 'latitude', 'longitude', 'parameters']
                              )
    return df_index



def filter_index(df_index, lon0, lon1, lat0, lat1, date0, date1, bgc_parameters):
    """
    This function filters the index file by BGC parameters, longitudes, latitudes, and dates all at once.
    
    INPUT:
    * df_index: the original index file, which can be obtained by `load_index()`
    * lon0, lon1, lat0, lat1: the east, west, south, and north edges of the spatial domain
    * date0, date1: the beginning and end of the temporal coverage (string: 'YYYY-MM-DD')
    * bgc_parameters: the list of BGC parameters (string or list)

    OUTPUT:
    * df_index_out: the filtered index file
    """
    
    # Filter by parameters
    df_index_out = df_index.copy()
    for param in bgc_parameters:
        df_index_out = df_index_out[df_index_out['parameters'].str.contains(param)]
    
    # Filter by longitudes    
    if lon0 > lon1:
        raise ValueError(f"lon0 cannot be greater than lon1.")
    else:
        if lon0 > 180 or lon1 > 180:
            if lon0 < 0 or lon1 < 0:
                raise ValueError(
                    f"lon0 and lon1 cannot be a mixture of <0 and >180." 
                    f" You entered: {lon0} and {lon1}."
                    f" Use either the -180 to 180 system or the 0 to 360 system."
                )
            else:
                # for the 0 to 360 system
                df_index_out = df_index_out[(df_index_out['longitude'] % 360 >= lon0) & (df_index_out['longitude'] % 360 <= lon1)] 
        else:
            # for the -180 to 180 system
            df_index_out = df_index_out[(df_index_out['longitude'] >= lon0) & (df_index_out['longitude'] <= lon1)] 
    
    # Filter by latitudes
    if lat0 > lat1:
        raise ValueError(f"lat0 cannot be greater than lat1.")
    else:
        # Filter by latitudes
        df_index_out = df_index_out[(df_index_out['latitude'] >= lat0) & (df_index_out['latitude'] <= lat1)]

    # Check dates
    if date0 > date1:
        raise ValueError(f"date0 cannot be greater than date1.")
    
    # For some reason, there are profiles with missing dates. Remove them first.
    df_index_out = df_index_out[df_index_out['date'] >= 0]
    
    # Convert date from float64 to string
    df_index_out['date_str'] = df_index_out['date'].astype('int64').astype(str)
    
    # Convert the string to a proper datetime object
    df_index_out['datetime'] = pd.to_datetime(df_index_out['date_str'], format='%Y%m%d%H%M%S')
    
    # Filter by dates
    df_index_out = df_index_out[(df_index_out['datetime'] >= f'{date0} 00:00:00') & (df_index_out['datetime'] <= f'{date1} 23:59:59')]
    
    # Delete the columns `date` and `date_str` which are no longer needed
    del df_index_out['date']
    del df_index_out['date_str']

    # Add WMO
    df_index_out['wmo'] = df_index_out['file'].str.split('/').str[1]
    
    return df_index_out


def calculate_float_speed(lon, lat, date):
    """
    This function calculates a rough estimate for the float's drift speed at parking depth, which is typically at 1,000 m.
    NOTE that this represents the overall mean speed and not the mean of the instantaneous speed (between cycles). 
    This prevents from division by zero when there are multiple sampling (especially in the first day of deployment).

    INPUT:
    * lon: longitudes of the profiles (array)
    * lat: latitiudes of the profiles (array)
    * date: dates of the profiles (array)

    OUTPUT:
    * speed: the roughly estimated drift speed of the float (m/s)
    """
    
    # Earth's radius in meters
    R = 6371000  
    # convert to radians
    lon_rad = np.radians(np.array(lon))
    lat_rad = np.radians(np.array(lat))
    # take the difference
    delta_lon = lon_rad[1:] - lon_rad[:-1]
    delta_lat = lat_rad[1:] - lat_rad[:-1]
    # Haversine formula
    a = np.sin(delta_lat / 2)**2 + np.cos(lat_rad[:-1]) * np.cos(lat_rad[1:]) * np.sin(delta_lon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distances = R * c  # in meters
    # Time differences in days
    time_deltas = (np.array(date)[1:] - np.array(date)[:-1]).astype('timedelta64[D]').astype(int)
    # Speed in meters per second
    speed = np.sum(distances) / np.sum(time_deltas) / 86400.
    # average speed
    return speed


def map_and_timeline(df_index, lon0, lon1, lat0, lat1, mindays, minfreq, maxdrift, note=None):

    plt.close('all')
    
    # --- 1. Map and Plot Setup ---
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1, projection=ccrs.PlateCarree())
    ax1.add_feature(cft.LAND)
    ax1.set_extent([lon0, lon1, lat0, lat1], crs=ccrs.PlateCarree())
    gl = ax1.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False, color="None")
    gl.top_labels = False
    gl.right_labels = False
    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1,1,1)
    
    # We use a colormap called 'tab10' which gives 10 different colors.
    list_cmap = plt.colormaps['tab10'].colors
    
    # Initialize the count for floats passing the three criteria
    ind_pass = 0
    daimei = []
    
    for wmo, group in df_index.groupby('wmo'):
        
        # Sort the group by time just to be safe
        group = group.sort_values('datetime')
        
        # Ignore if there is only one profile
        if len(group) == 1:
            continue
    
        # Check criteria
        valid_freq = group['datetime'].diff().max() < pd.to_timedelta(minfreq, unit='D')
        valid_drift = calculate_float_speed(group['longitude'], group['latitude'], group['datetime']) < maxdrift
        valid_dur = (group['datetime'].max() - group['datetime'].min()) > pd.to_timedelta(mindays, unit='D')
    
        # If it passes all criteria, plot and save!
        if valid_freq and valid_drift and valid_dur:
            iro = list_cmap[ind_pass % len(list_cmap)]
            
            # Plot Map (ax1)
            ax1.scatter(group['longitude'], group['latitude'], color=iro, 
                        transform=ccrs.PlateCarree(), zorder=3, s=0.1)
            ax1.scatter(group['longitude'].iloc[-1], group['latitude'].iloc[-1], color='k', 
                        marker='.', transform=ccrs.PlateCarree(), zorder=4, s=6)
            ax1.text(group['longitude'].iloc[-1], group['latitude'].iloc[-1], str(ind_pass+1), color='k', 
                     transform=ccrs.PlateCarree(), zorder=5, fontsize=5)
            
            # Plot Time Series (ax2)
            ax2.scatter(group['datetime'], [ind_pass]*len(group), color=iro, marker='|', linewidths=0.5)
            
            # label for time series figure
            daimei.append(f"{wmo}({ind_pass+1})")        
            
            ind_pass += 1
    
    # Save the current time for creating a unique id for the figures.
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    fig.tight_layout()
    
    ax2.set_yticks(range(len(daimei)))
    ax2.set_yticklabels(daimei)
    ax2.set_xlim(datetime.strptime(str(date0), '%Y-%m-%d'), datetime.strptime(str(date1), '%Y-%m-%d'))
    ax2.set_ylabel('WMO (label on the map)')
    fig2.tight_layout()

    # Save the figures
    if note:
        fig.savefig(f'map_search_{note}_{now}', dpi=300, bbox_inches='tight')
        fig2.savefig(f'timeline_search_{note}_{now}', dpi=300, bbox_inches='tight')
    else:
        fig.savefig(f'map_search_{now}', dpi=300, bbox_inches='tight')
        fig2.savefig(f'timeline_search_{now}', dpi=300, bbox_inches='tight')
# Lessons [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hakaseh/bgc-argo-tutorials/HEAD)

This folder contains the following lessons and functions (* means that the argument is optional):

* **Lesson 1**: 🔍 Search for floats 
    * load_index()
    * filter_index(df_index, lon0, lon1, lat0, lat1, date0, date1, bgc_parameters, bgc_mode)
    * calculate_float_speed(lon, lat, date)
    * filter2_and_save_index(df_index, mindura*, minfreq*, maxdrif*, note*)
* **Lesson 2**: 🎨 Maps and timelines
    * load_filtered_index(file_path)
    * show_map_timeline(df_index, note*, mapsize*, timelinesize*)
* **Lesson 3**: ⬇️ Download
    * download_argo(df_index, wmoid_input*)
* **Lesson 4**: ✅ QC flags
    * time_and_dt(ds)
    * filter_qc(ds_in, name_in, qc_in)
    * plot_2d_heatmap(ds_in, var_list_in, qc_in*)
* **Lesson 5**: 🪄 Interpolation
    * init_ds_interp(ds_ori, dep0*, dep1*, ddep*)
    * interp_and_update(da_var_in, da_pres_in, ds_out)
* **Lesson 6**: ➕ Additional variables
    * derive_and_add(ds)

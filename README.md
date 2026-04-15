# bgc-argo-tutorials: A practical guide to biogeochemical Argo data analysis [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hakaseh/bgc-argo-tutorials/HEAD)

`bgc-argo-tutorials` provides a series of lessons on the analysis of biogeochemical Argo (BGC-Argo) data written in Python and Jupyter Notebook. Specifically, `bgc-argo-tuorials` teaches you how to search, identify, download, visualize, and post-process the vertical profiles of physical and biogeochemical oceanographic variables measured by autonomous floats in the global ocean. An overview of `bgc-argo-tutorials` is provided as [a peer-reviewed article](https://jose.theoj.org/) in the Journal of Open Source Education. If you find `bgc-argo-tutorials` useful, please consider citing our paper:

`Fujishima, H. and Hayashida, H. (submitted): bgc-argo-tutorials: A practical guide to biogeochemical Argo data analysis, Journal of Open Source Education.`

**🚨 Ready to dive into BGC-Argo data but not sure where to begin? Give `bgc-argo-tutorials` a try!**

---

## 🚀 Getting Started
To try `bgc-argo-tutorials`, click on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hakaseh/bgc-argo-tutorials/HEAD), which allows you to test our Jupyter Notebooks (i.e., lessons) on cloud. This is useful if you do not have a Jupyter environment or if you just want to check out `bgc-argo-tutorials` before installing them.

To install `bgc-argo-tutorials` on your local system, the best way is to use `git` for keeping your copy up to date with the source.

## 🛠️ Installation and Setup
We highly recommend using `conda` to manage your Python environment, as it automatically handles the complex system-level dependencies required for oceanographic mapping tools (like `cartopy`). However, if your institution restricts `conda`, we also provide a standard `pip` installation method.

### Option 1: Using Conda (Recommended)

1. Clone the repository and navigate into it:
    ```
    git clone https://github.com/your-username/bgc-argo-tutorials.git
    cd bgc-argo-tutorials
    ```

1. Create the environment from the provided YAML file:
    ```
    conda env create -f environment.yml
    ```

1. Activate the environment:
    ```
    conda activate bgc-argo-tutorials
    ```

### Option 2: Using Pip (For Non-Conda Users)

1. Create a Python virtual environment:

    ```
    python -m venv env
    ```

1. Activate the virtual environment:

    On macOS and Linux:
    ```
    source env/bin/activate
    ```

    On Windows:
    ```
    env\Scripts\activate
    ```

1. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

    🚨 **A note on cartopy for pip users:** The cartopy mapping library requires underlying system binaries (specifically GEOS and PROJ). While pip usually installs pre-compiled versions successfully, older or highly restricted operating systems might throw compiler errors. If this happens, you may need to install the geos and proj system binaries locally before pip install will work.

### Final step (common to both options)

Register this specific environment as a permanent Jupyter kernel:
```
python -m ipykernel install --user --name=env --display-name "bgc-argo-tutorials"
```

Finally, launch Jupyter (e.g., `jupyter notebook` or `jupyterlab`), open `lesson_01.ipynb`, and select the `bgc-argo-tutorials` environment from the notebook's drop-down menu. You are all set!

## Directory Structure
`bgc-argo-tutorials` consists of the following folders:

* **lessons** contains the main Jupyter Notebook tutorials.
* **index_files** contains customized index files generated in Lesson 1.
* **figures** contains figures generated in Lesson 2/.
* **floats** contains the float time series and individual profiles downloaded in Lesson 3 and the interpolated time series generated in Lesson 5/6. 


## 🗳️ Feedback 
We want to hear your thoughts! Please feel free to provide your user experience by visiting [this link](https://forms.gle/oAGmz5RTW4Pp46bt7). Your feedback will help us improve the contents of `bgc-argo-tutorials`.

## ☎️ Contact 
For questions and comments, feel free to create a new issue or replying to an existing one by visiting [Issues](https://github.com/hakaseh/bgc-argo-tutorials/issues). Alternatively, you may send a message to [@hakaseh](https://github.com/hakaseh).

## 📚 Resources
- [Argo Online School](https://euroargodev.github.io/argoonlineschool/intro.html)
- [Wong et al. 2020](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2020.00700/full): this paper provides an overview of Argo
- [Claustre et al. 2020](https://doi.org/10.1146/annurev-marine-010419-010956): this paper provides an overview of BGC-Argo
- [OceanOPS Argo map](https://www.ocean-ops.org/maps/static/?t=Argo)
- [Argo fleet monitoring](https://fleetmonitoring.euro-argo.eu/dashboard)
- [Peer reviewed articles using BGC-Argo](https://biogeochemical-argo.org/peer-review-articles-data-table-stat.php)

## 🗃️ Old Repo
`bgc-argo-tutorials` was initially hosted on Gitlab, but was later moved to Github for the JOSE submission. We kept the old repository for reference to [issues](https://gitlab.com/evparg/analysis-ready-bgc-argo-dataset/-/issues).

## 🇯🇵　日本語 (Japanese Language Support)
`bgc-argo-tutorials`では、日本語によるサポートやワークショップも実施しております。お気軽にお問い合わせください（海洋研究開発機構　林田博士）。
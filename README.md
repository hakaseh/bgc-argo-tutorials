# bgc-argo-tutorials: An interactive Jupyter Notebook guide to biogeochemical Argo data [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hakaseh/bgc-argo-tutorials/HEAD)

[:japan: 日本語はこちら](#生物地球化学アルゴチュートリアル)

`bgc-argo-tutorials` is a series of Jupyter Notebook tutorials that serves as a tutorial for post-processing biogeochemical Argo (BGC-Argo) float time series. searching, downloading, and post-processing the concatenated synthetic-profile time series of BGC-Argo floats.

To use these templates, simply create a copy (and rename it), modify the user inputs, and run it on your Jupyter environment. **But please remember to cite the following paper to make us happy 😃:**

`Fujishima, H. and Hayashida, H. (in prep): bgc-argo-tutorials: An interactive Jupyter Notebook guide to biogeochemical Argo data, Journal of Open Source Education.`

## Contents
`bgc-argo-tutorials` consists of three Jupyter Notebook templates that do the following:

- Search for BGC-Argo float(s) of your interest (`search.ipynb`)
- Download the concatenated synthetic-profile time series of a selected float (`download.ipynb`)
- Generate the analysis-ready BGC-Argo float time series of a selected float (`generate.ipynb`)

### `search.ipynb` 🗺️
***You can skip this notebook if you already have specific float(s) in mind***
`search.ipynb` searches for BGC-Argo floats based on the user's selection criteria such as spatial coverage, time period, and variables.

`search.ipynb` may be particularly useful for users who are looking for floats that collected profiles:
- at least for a specific duration (e.g., 365 days, if you study an annual cycle). Modify `mindays`.
- at a specific sampling frequency (e.g., 7 days, if you study a weekly variability). Modify `minfreq`.
- at a specific drift speed (e.g., 0.05 m/s, if you study quasi-Eulerian )

If none of the above are relevant, we recommend other tools such as [Argo Fleet Monitoring](https://fleetmonitoring.euro-argo.eu/dashboard?Status=Active), which may be easier to use for searching.

### `download.ipynb` 💻
***You can skip this notebook if you have already downloaded the concatenated synthetic-profile time series (e.g., 1234567_Sprof.nc) of your favorite float.***

`download.ipynb` downloads the synthetic-profile time series of your choice. You need to specify the float's 7-digit WMOID.

### `generate.ipynb` 🍰
This is the main notebook, which post-processes the raw data by filtering, smoothing, and interpolation to make them "analysis-ready". Specifically, it will take the following steps and produces figures (*.png) and a netCDF file at the end:
1. Read raw profiles (e.g. `1234567_Sprof.nc`).
1. Filter using Quality Control (QC) values (default: 1, 2, 5, 8).
1. Smooth CHLA_ADJUSTED based on Schmechtig et al. (2023).
1. Decompose BBP700_ADJUSTED into BBP700SM_ADJUSTED (<100 um) and BBP700LG_ADJUSTED (>100 um) based on Briggs et al. (2020).
1. Interpolate based on Akima (1970) (default resolution = 5 dbar, which is about [the uncertainty of pressure measurements](https://argo.ucsd.edu/data/data-faq/#accurate)). 
1. Apply NPQ correction to CHL_ADJUSTED based on Xing et al. (2012).
1. Derive additional variables using TEOS-10 (GSW-Python).
1. Save the analysis-ready profiles as a netCDF file (e.g., `AR1234567.nc`).

## Variables

### Measured variables
| Variable | Units | Uncertainty |
| ------ | ------ | ------ |
| Temperature | $^{\circ}$C | [0.002 $^{\circ}$C](https://argo.ucsd.edu/data/data-faq/#accurate) |
| Salinity | psu | [0.01 psu](https://argo.ucsd.edu/data/data-faq/#accurate) |
| PAR | W m$^{-2}$ | ? |
| Nitrate | $\mu$mol kg$^{-1}$ | 0.5 $\mu$mol kg$^{-1}$ |
| Chlorophyll-a | mg m$^{-3}$ | 50 % |
| BBP700 | m$^{-1}$ | 20 % |
| Oxygen | $\mu$mol kg$^{-1}$ | 1 % |
| pH | n.d. | 0.015 |

### Derived varaibles
| Variable | Units | Derived from | Methods |
| ------ | ------ | ------ | ------ |
| MLD | m | Sigma0 | [TEOS-10](https://teos-10.github.io/GSW-Python/gsw_flat.html) |
| SIGMA0 | kg m$^{-3}$ | T, S | [TEOS-10](https://teos-10.github.io/GSW-Python/gsw_flat.html) |
| SPICINESS0 | kg m$^{-3}$ | T, S | [TEOS-10](https://teos-10.github.io/GSW-Python/gsw_flat.html) |
| O2SOL | $\mu$mol kg$^{-1}$ | T, S | [TEOS-10](https://teos-10.github.io/GSW-Python/gsw_flat.html) |
| BBP700SM | m$^{-1}$ | BBP700 | [Briggs et al. 2020](https://science.sciencemag.org/content/367/6479/791) |
| BBP700LG | m$^{-1}$ | BBP700 | [Briggs et al. 2020](https://science.sciencemag.org/content/367/6479/791) | 

## Getting started
1. Download the repository via `git clone` or by clicking on **Code** (in blue) above and choose **Download source code** (e.g., as a zip file).
1. Start a Jupyter session (`jupyter notebook` or `jupyter lab`). Alternatively, you can use a GUI version (e.g., [Anaconda Navigator](https://www.anaconda.com/products/navigator)).
1. Create a copy of the template you want to use and open the copied notebook.
1. Modify the input based on your need and run through the notebook.

## Feedback
We want to hear your thoughts! Please feel free to provide your user experience by visiting [this link](https://forms.gle/oAGmz5RTW4Pp46bt7). Your feedback will help us improve the contents of `bgc-argo-tutorials`.

## Contact
Please feel free to message [@hakaseh](https://github.com/hakaseh). We also welcome creating new issues or contributing to existing ones ([Issues](https://github.com/hakaseh/bgc-argo-tutorials/issues)).

## Notes

### Old repository
`ar-bgc-argo` was initially hosted on Gitlab, but was later moved to Github for the JOSS submission. We kept the old repository for reference to [issues](https://gitlab.com/evparg/analysis-ready-bgc-argo-dataset/-/issues).


### Key references and useful websites
- [Wong et al. 2020](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2020.00700/full): this paper provides an overview of Argo
- [Claustre et al. 2020](https://doi.org/10.1146/annurev-marine-010419-010956): this paper provides an overview of BGC-Argo
- [OceanOPS Argo map](https://www.ocean-ops.org/maps/static/?t=Argo): for Argo float coverage
- [Argo fleet monitoring](https://fleetmonitoring.euro-argo.eu/dashboard): floats
- [Peer reviewed articles using BGC-Argo](https://biogeochemical-argo.org/peer-review-articles-data-table-stat.php)

---

# 生物地球化学アルゴチュートリアル

`bgc-argo-tutorials`は、生物地球化学アルゴ(BGC-Argo)フロートのsynthetic-profile時系列を"解析可能"な状態にデータセットを創出するJupyter Notebookを提供しています。

ノートブックを使われる際は、以下の文献の引用をお願いいたします 🙇：

`Fujishima, H. and Hayashida, H. (submitted): ar-bgc-argo: Jupyter Notebook templates for searching, downloading, and post-processing biogeochemical Argo float time series, Journal of Open Source Software.`

## 構成
このレポジトリは以下のJupyter Notebookで構成されています：

- ユーザーのニーズに合ったフロートを検索する (`search.ipynb`)
- 選択したフロートのプロファイルを一括ダウンロードする (`download.ipynb`)
- ダウンロードしたプロファイル一式を処理し、解析可能なデータセットを創出 (`generate.ipynb`)

### search.ipynb
***前処理したいフロートがすでに決まっている場合はこのノートブックを実行する必要はありません***

フロートを検索するためにユーザーが指定できる項目：
- 緯度・経度の範囲：
- 期間：
- 観測頻度：
- 軌道速度：フロートのプロファイリング時の緯度・経度・日時を元に見積られた総移動距離を総移動時間で割って算出
- 観測変数：下記６つの[観測変数](###観測変数)から選択

### `download.ipynb`
***前処理したいフロートのプロファイルをすでにダウンロードしている場合はこのノートブックを実行する必要はありません***

このノートブックは、`wget`というコマンドを用いてユーザーが指定したフロートの[Sプロファイル](https://argo.ucsd.edu/data/data-faq/#v3core)を一括ダウンロードします。

### `generate.ipynb`
このノートブックは、ダウンロードしたプロファイル一式に前処理を施して解析可能な鉛直時系列を創出します。具体的には次の順に処理され各ステップで図(PNG形式)が作成されます。そして最後にnetCDFファイルが創出されます:

1. 全データを可視化 `fig-raw-*.png`
1. 品質管理(QC)フラグをもとに良データのみを可視化 (良データと考えられるQCフラグのデフォルト値: 1, 2, 5, 8) 
1. N点中央値フィルタで平滑化(Nは鉛直解像度をもとに決定；[Schmechtig et al. 2023](https://archimer.ifremer.fr/doc/00243/35385/)) 
1. 指定した鉛直解像度と深度範囲で内挿 (デフォルト解像度：5 dbar, [深度観測の基準誤差](https://argo.ucsd.edu/data/data-faq/#accurate)). 
1. その他、補正および導出変数の計算 
1. netCDF形式で鉛直時系列データを保存。ファイル名は`AR[WMOID].nc` (`AR`はAnalysis-Readyの略で`[WMOID]`フロート番号)

## 変数

### 観測変数
| 変数 | 単位 | 不確実性 |
| ------ | ------ | ------ |
| 水温 | $^{\circ}$C | [0.002 $^{\circ}$C](https://argo.ucsd.edu/data/data-faq/#accurate) |
| 塩分 | psu | [0.01 psu](https://argo.ucsd.edu/data/data-faq/#accurate) |
| 光合成有効放射 (PAR) | W m$^{-2}$ | ? |
| 硝酸塩 | $\mu$mol kg$^{-1}$ | 0.5 $\mu$mol kg$^{-1}$ |
| クロロフィルa | mg m$^{-3}$ | 50 % |
| 700nm粒子後方散乱係数 | m$^{-1}$ | 20 % |
| 溶存酸素 | $\mu$mol kg$^{-1}$ | 1 % |
| pH | n.d. | 0.015 |

### 導出変数
| 変数 | 単位 | 原変数 | 手法 |
| ------ | ------ | ------ | ------ |
| ポテンシャル密度アノマリ | kg m$^{-3}$ | 水温、塩分 | [TEOS-10](https://teos-10.github.io/GSW-Python/gsw_flat.html) |
| 混合層深度 | m | ポテンシャル密度アノマリ | [TEOS-10](https://teos-10.github.io/GSW-Python/gsw_flat.html) |
| スパイシネス | kg m$^{-3}$ | 水温、塩分 | [TEOS-10](https://teos-10.github.io/GSW-Python/gsw_flat.html) |
| 酸素飽和度 | $\mu$mol kg$^{-1}$ | 水温、塩分 | [TEOS-10](https://teos-10.github.io/GSW-Python/gsw_flat.html) |
| 小さい粒子 | m$^{-1}$ | 700nm粒子後方散乱係数 | [Briggs et al. 2020](https://science.sciencemag.org/content/367/6479/791) |
| 大きい粒子 | m$^{-1}$ | 700nm粒子後方散乱係数 | [Briggs et al. 2020](https://science.sciencemag.org/content/367/6479/791) | 


## 使い方 📘
1. レポジトリをダウンロードする。コマンドラインの場合、`git clone`。それ以外の場合は、ページ上部の**Code（青色のアイコン）**→**Download source code**をクリックしてZipファイルとしてダウンロードする。
1. Jupyterを起動する。コマンドラインの場合、`jupyter notebook`または`jupyter lab`。それ以外の場合は、例えば[Anaconda Navigator](https://www.anaconda.com/products/navigator))を使用する。
1. 使いたいノートブックのコピーを作る（例：`search-Copy.ipynb`）。コピーしたノートブックは元のノートブックと同じディレクトリに置く。
1. ノートブックを開いて`User input begins`から`User input ends`の間の部分をカスタマイズしてノートブックを実行する。

## 連絡先 ✋
質問やコメントは、[@hakaseh](https://github.com/hakaseh)まで。[Issues](https://github.com/hakaseh/ar-bgc-argo/issues)への投稿も歓迎します。

## 補足
### 古いレポ
`ar-bgc-argo`は以前はGitlabで管理していましたが、JOSS投稿のためにGithubに異動しました。参考のために古いレポは消さずに[issues](https://gitlab.com/evparg/analysis-ready-bgc-argo-dataset/-/issues)は閲覧できるようにしてあります。

### 参考文献・Webサイト
- [Wong et al. 2020](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2020.00700/full): Argo計画の概要論文
- [Claustre et al. 2020](https://doi.org/10.1146/annurev-marine-010419-010956): BGC-Argoの概要論文
- [OceanOPS Argo map](https://www.ocean-ops.org/maps/static/?t=Argo): 月毎の全球フロート観測網の可視化
- [Argo fleet monitoring](https://fleetmonitoring.euro-argo.eu/dashboard): 各フロートの詳細を調べられるサイト
- [Argo計画・日本公式サイト](https://www.jamstec.go.jp/J-ARGO/)：研究成果登録にご協力をお願いいたします。


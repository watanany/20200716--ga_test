# Google Analyticsのテスト

## セットアップ

```
$ conda env create -n ga_test
$ source activate ga_test
```

### pyenv + virtualenv + miniconda3-latestの場合

```
$ pyenv install miniconda3-latest
$ pyenv local miniconda3-latest
$ conda env create -n ga_test

$ source $PYENV_ROOT/versions/miniconda3-latest/bin/activate ga_test
または
$ source $PYENV_VIRTUAL_ENV/bin/activate ga_test
```

## ディレクトリ構成
<dl>
  <dt>environment.yaml</dt>
  <dd>conda の環境ファイル</dd>

  <dt>lib/get_print.py</dt>
  <dd>Google Analyticsからデータを取り込み、標準出力に出力する</dd>

  <dt>lib/calc.py</dt>
  <dd>
    KMeans + 遺伝的アルゴリズムでクラスタリングを行なう<br>
    lib/get_print.py 出力を output/views.csv に出力していることを前提とする
  </dd>
</dl>

## 参考URL
* [レポートツール - アナリティクス ヘルプ](https://support.google.com/analytics/topic/6175347?hl=ja&ref_topic=1727148 "レポートツール - アナリティクス ヘルプ")
* [はじめてのアナリティクス Reporting API v4: インストール済みアプリケーション向け Python クイックスタート  |  アナリティクス Reporting API v4  |  Google Developers](https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/installed-py "はじめてのアナリティクス Reporting API v4: インストール済みアプリケーション向け Python クイックスタート  |  アナリティクス Reporting API v4  |  Google Developers")
* [Google アナリティクス Reporting API  |  アナリティクス Reporting API v4  |  Google Developers](https://developers.google.com/analytics/devguides/reporting/core/v4/rest/ "Google アナリティクス Reporting API  |  アナリティクス Reporting API v4  |  Google Developers")
* [Dimensions & Metrics Explorer  |  アナリティクス Reporting API v4  |  Google Developers](https://developers.google.com/analytics/devguides/reporting/core/dimsmets "Dimensions & Metrics Explorer  |  アナリティクス Reporting API v4  |  Google Developers")

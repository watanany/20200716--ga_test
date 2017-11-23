# Google Analyticsのテスト

## ディレクトリ構成
requirements.yaml
  : conda の環境ファイル

lib/get\_print.py
  : Google Analyticsからデータを取り込み、標準出力に出力する

lib/calc.py
  : KMeans + 遺伝的アルゴリズムでクラスタリングを行なう
    lib/get\_print.py 出力を output/views.csv に出力していることを前提とする

## 参考URL
* [レポートツール - アナリティクス ヘルプ](https://support.google.com/analytics/topic/6175347?hl=ja&ref_topic=1727148 "レポートツール - アナリティクス ヘルプ")
* [はじめてのアナリティクス Reporting API v4: インストール済みアプリケーション向け Python クイックスタート  |  アナリティクス Reporting API v4  |  Google Developers](https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/installed-py "はじめてのアナリティクス Reporting API v4: インストール済みアプリケーション向け Python クイックスタート  |  アナリティクス Reporting API v4  |  Google Developers")
* [Google アナリティクス Reporting API  |  アナリティクス Reporting API v4  |  Google Developers](https://developers.google.com/analytics/devguides/reporting/core/v4/rest/ "Google アナリティクス Reporting API  |  アナリティクス Reporting API v4  |  Google Developers")
* [Dimensions & Metrics Explorer  |  アナリティクス Reporting API v4  |  Google Developers](https://developers.google.com/analytics/devguides/reporting/core/dimsmets "Dimensions & Metrics Explorer  |  アナリティクス Reporting API v4  |  Google Developers")

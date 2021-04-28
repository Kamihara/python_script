#!/usr/bin/python
# coding: utf-8

import urllib.request
import urllib.parse

API = "http://api.aoikujira.com/zip/xml/get.php"

# パラメータをURLエンコードする
values = {
    'fmt': 'xml',
    'zn': '1500042'
}
params = urllib.parse.urlencode(values)

# リクエスト用のURLを生成
url = API + "?" + params
print("url=", url)

# ダウンロード
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)

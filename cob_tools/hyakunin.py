#!/usr/bin/env python3
# coding: utf-8

import sys
import urllib.request as req
import urllib.parse as parse

# コマンドライン引数ｗｐ取得
if len(sys.argv) <= 1:
    print("Usage: hyakunin.py (keyword)")
    sys.exit
keyword = sys.argv[1]

# パラメータをURLエンコードする
API = "http://api.aoikujira.com/hyakunin/get.php"
query = {
    'fmt': 'ini',
    'key': keyword
}
params = parse.urlencode(query)
url = API + "?" + params
print("url=", url)

# ダウンロード
with req.urlopen(url) as r:
    b = r.read()
    data = b.decode('utf-8')
    print(data)

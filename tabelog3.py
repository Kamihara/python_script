#!/usr/bin/python
# coding: utf-8

import sys
import json
import time
import csv
from bs4 import BeautifulSoup
import urllib.request as req
from urllib.parse import urljoin

################################################################
# 関数定義
################################################################
# データ構成
# shopinfolist[0] : url
# shopinfolist[1] : json


def print_shopinfo(shopinfolist):
    for l in shopinfolist:
        print(l[0])
        print(l[1])


################################################################
# メイン処理
################################################################
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    with open('shopinfolist.txt', 'r') as f:
        reader = csv.reader(f)

        for r in reader:
            print(type(r))
            print(r)

    print_shopinfo(reader[0])
#!/usr/bin/python
# coding: utf-8

import sys
import time
import csv
from bs4 import BeautifulSoup
import urllib.request as req
from urllib.parse import urljoin

################################################################
# 関数定義
################################################################
# 店舗基本情報の取得
def get_shopinfo(urllist):
    shopinfo_list = []
    for url in urllist:
        time.sleep(1)
        res = req.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        shopbaseinfo = soup.find("script", attrs={"type": "application/ld+json"})
        shopbaseinfo_json = shopbaseinfo.string.strip()
        shopinfo_list.append([url, shopbaseinfo_json])
        print(shopbaseinfo_json)
    return shopinfo_list

################################################################
# メイン処理
################################################################
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    shopurllist = []

    with open('shopurllist.csv', 'r') as ci:
        csvreader = csv.reader(ci)
        for csv in csvreader:
            for c in csv:
                shopurllist.append(c)

    # 店舗基本情報取得
    shopinfolist = get_shopinfo(shopurllist)

    # 店舗基本情報をファイルへ出力
    with open('shopinfolist.txt', 'w') as f:
        for info in shopinfolist:
            f.write(str(info) + '\n')

    with open('shopinfolist.csv', 'w') as co:
        csvwriter = csv.writer(co)
        for line in shopinfolist:
            csvwriter.writerow(line)

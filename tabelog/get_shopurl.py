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
# 店舗URLリストの取得
def get_shopurl_list(url):
    shopurl_list = []
    while(True):
        # 一覧ページ内のurl20件を取得する
        res1 = req.urlopen(url)
        time.sleep(1)
        soup = BeautifulSoup(res1, "html.parser")
        shoplist = soup.find_all("a", attrs={"class": "list-rst__rst-name-target"})

        for shop in shoplist:
            shopurl = shop.attrs['href']
            shopurl_list.append(shopurl)
            print(shopurl)

        # 次の20件ページを取得する
        res2 = req.urlopen(url)
        # 次の20件へのリンクを取得
        soup2 = BeautifulSoup(res2, "html.parser")
        ln = soup2.find("a", attrs={"class": "page-move__target--next"})
        if ln == None:
            # 最終ページに到達したら終了
            break
        else:
            url = ln.attrs['href']

    return shopurl_list

################################################################
# メイン処理
################################################################
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]
    # 一覧ページの1ページ目
    url = args[1]

    # 店舗URL全件取得
    shopurllist = get_shopurl_list(url)

    # 店舗URLをファイルへ出力
    with open('shopurllist.txt', 'w') as f:
        for url in shopurllist:
            f.write(url + '\n')

    with open('shopurllist.csv', 'w') as c:
        csvwriter = csv.writer(c)
        csvwriter.writerow(shopurllist)

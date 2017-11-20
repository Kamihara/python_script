#!/usr/bin/python
# coding: utf-8

import sys
import time
import csv
from bs4 import BeautifulSoup
import urllib.request as req

################################################################
# 関数定義
################################################################
# 店舗URLリストの取得
def get_shopurl_list(url):
    shopurl_list = []
    while(True):
        # 一覧ページ内のurl20件を取得する
        res1 = req.urlopen(url)
        time.sleep(5)
        soup = BeautifulSoup(res1, "html.parser")
        shoplist = soup.find_all("a", attrs={"class": "list-rst__rst-name-target"})

        for shop in shoplist:
            shopurl = shop.attrs['href']
            shopurl_list.append(shopurl)
            print(shopurl)

        # 次の20件へのリンクを取得
        ln = soup.find("a", attrs={"class": "c-pagination__arrow--next"})
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
    dir = args[1]
    url = args[2]

    # filename = "area_urllist.txt"
    #
    # f = open("./" + dir + "/" + filename, "r")
    # lines = f.readlines()
    # f.close()

    url12 = url.replace("LstCos=0&LstCosT=1", "LstCos=1&LstCosT=2")
    url23 = url.replace("LstCos=0&LstCosT=1", "LstCos=2&LstCosT=3")
    url34 = url.replace("LstCos=0&LstCosT=1", "LstCos=3&LstCosT=4")
    url45 = url.replace("LstCos=0&LstCosT=1", "LstCos=4&LstCosT=5")
    url56 = url.replace("LstCos=0&LstCosT=1", "LstCos=5&LstCosT=6")
    url67 = url.replace("LstCos=0&LstCosT=1", "LstCos=6&LstCosT=7")
    url78 = url.replace("LstCos=0&LstCosT=1", "LstCos=7&LstCosT=8")
    url89 = url.replace("LstCos=0&LstCosT=1", "LstCos=8&LstCosT=9")
    url910 = url.replace("LstCos=0&LstCosT=1", "LstCos=9&LstCosT=10")
    url1011 = url.replace("LstCos=0&LstCosT=1", "LstCos=10&LstCosT=11")
    url1112 = url.replace("LstCos=0&LstCosT=1", "LstCos=11&LstCosT=0")

    lines = []
    lines.append(url)
    lines.append(url12)
    lines.append(url23)
    lines.append(url34)
    lines.append(url45)
    lines.append(url56)
    lines.append(url67)
    lines.append(url78)
    lines.append(url89)
    lines.append(url910)
    lines.append(url1011)
    lines.append(url1112)

    for line in lines:
        print(line)

    for l in lines:
        # 店舗URL全件取得
        shopurl_list = get_shopurl_list(l)

        # 店舗URLをファイルへ出力
        with open(dir + '/shopurl_list.txt', 'a') as c:
            cw = csv.writer(c, delimiter='\n')
            cw.writerow(shopurl_list)

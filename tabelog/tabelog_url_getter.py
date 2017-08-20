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
        time.sleep(5)
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

# クチコミURLリストの取得
def get_kuchikomiurl_list(url):
    kuchikomiurl_list = []

    # 店舗クチコミURLをファイルへ出力
    with open('kuchikomiurllist.txt', 'w') as f:
        for u in url:
            kuchikomipage_url = u + "dtlrvwlst/"
            while(True):
                print(kuchikomipage_url)
                # 一覧ページ内のurl20件を取得する
                try:
                    res1 = req.urlopen(kuchikomipage_url)
                except Exception as e:
                    print(e)
                    break

                time.sleep(5)
                soup = BeautifulSoup(res1, "html.parser")
                kuchikomi_list = soup.find_all("a", attrs={"class": "rvw-item__title-target"})

                for kuchikomi in kuchikomi_list:
                    kuchikomi_url = kuchikomi.attrs['href']
                    kurl = urljoin(u, kuchikomi_url)
                    kuchikomiurl_list.append(kurl)
                    f.write(kurl + '\n')
                    print(kurl)

                # 次の20件ページを取得する
                try:
                    res2 = req.urlopen(kuchikomipage_url)
                except Exception as e:
                    print(e)
                    break

                # 次の20件へのリンクを取得
                soup2 = BeautifulSoup(res2, "html.parser")
                ln = soup2.find("a", attrs={"class": "page-move__target--next"})
                if ln == None:
                    # 最終ページに到達したら終了
                    break
                else:
                    kuchikomipage_url = urljoin(u, ln.attrs['href'])

    return kuchikomiurl_list


################################################################
# メイン処理
################################################################
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]
    # 一覧ページの1ページ目
    url = args[1]
    dir = args[2]

    # 店舗URL全件取得
    shopurl_list = get_shopurl_list(url)

    # 店舗URLをファイルへ出力
    with open(dir + '/shopurl_list.csv', 'w') as c:
        cw = csv.writer(c)
        cw.writerow(shopurl_list)

    # 店舗クチコミURL全件取得
    kuchikomiurl_list = get_kuchikomiurl_list(shopurl_list)


    # 店舗URLをファイルへ出力
    with open(dir + '/kuchikomiurl_list.csv', 'w') as c:
        cw = csv.writer(c)
        cw.writerow(kuchikomiurl_list)

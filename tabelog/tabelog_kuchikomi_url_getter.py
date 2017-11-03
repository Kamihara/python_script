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
# クチコミURLリストの取得
def get_kuchikomiurl_list(url):
    kuchikomiurl_list = []

    # 店舗クチコミURLを収集しリスト形式で返却
    kuchikomipage_url = url.replace("\n", "") + "dtlrvwlst/"
    while(True):
        print(kuchikomipage_url)
        # 一覧ページ内のurl20件を取得する
        try:
            res1 = req.urlopen(kuchikomipage_url)
        except Exception as e:
            print(e)
            break

        soup = BeautifulSoup(res1, "html.parser")

        kuchikomi_list = soup.find_all("a", attrs={"class": "rvw-item__title-target"})

        for kuchikomi in kuchikomi_list:
            kuchikomi_url = kuchikomi.attrs['href']
            full_url = urljoin(url, kuchikomi_url)
            kuchikomiurl_list.append(full_url)
            print(full_url)

        # # 次の20件ページを取得する
        # try:
        #     res2 = req.urlopen(kuchikomipage_url)
        # except Exception as e:
        #     print(e)
        #     break

        # # 次の20件へのリンクを取得
        # soup2 = BeautifulSoup(res2, "html.parser")
        # ln = soup2.find("a", attrs={"class": "page-move__target--next"})
        ln = soup.find("a", attrs={"class": "c-pagination__arrow--next"})
        if ln == None:
            # 最終ページに到達したら終了
            break
        else:
            kuchikomipage_url = urljoin(url, ln.attrs['href'])
            time.sleep(5)

    return kuchikomiurl_list


################################################################
# メイン処理
################################################################
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]
    # 一覧ページの1ページ目
    dir = args[1]

    filename = "shopurl_list.txt"

    f = open("./" + dir + "/" + filename, "r")
    lines = f.readlines()
    f.close()

    for url in lines:
        # 店舗クチコミURL全件取得
        kuchikomiurl_list = get_kuchikomiurl_list(url)

        # 店舗クチコミURLをファイルへ出力
        with open(dir + '/kuchikomiurl_list.txt', 'a') as c:
            cw = csv.writer(c, delimiter='\n')
            cw.writerow(kuchikomiurl_list)

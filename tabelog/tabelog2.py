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
# クチコミ情報の取得
def get_kuchikomi_info(urllist):
    kuchikomiinfo_list = []
    with open('kuchikomiinfolist2.csv', 'w') as c:
        csvwriter = csv.writer(c)

        for url in urllist:
            img = []
            res = req.urlopen(url)
            time.sleep(3)
            soup = BeautifulSoup(res, "html.parser")

            shopname = soup.find("span", attrs={"class": "rstdtl-crumb"})
            kuchikomi_title = soup.find("p", attrs={"class": "rvw-item__title"})
            kuchikomi_text = soup.find("div", attrs={"class": "rvw-item__rvw-comment"})
            kuchikomi_img = soup.find_all("div", attrs={"class": "rvw-photo__list-img"})

            name = shopname.text
            title = kuchikomi_title.text
            text = kuchikomi_text.text
            for i in kuchikomi_img:
                imgurl = i.a.get('href')
                img.append(imgurl)

            kuchikomiinfo_list.append([url, name, title, text, img])
            csvwriter.writerow([url, name, title, text, img])
            print(text)

    return kuchikomiinfo_list

################################################################
# メイン処理
################################################################
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    with open('kuchikomiurllist2.txt') as f:
        kuchikomiurllist = f.readlines()

    # 店舗クチコミ情報取得
    kuchikomiinfolist = get_kuchikomi_info(kuchikomiurllist)

    # 店舗クチコミ情報をファイルへ出力
    with open('kuchikomiinfolist2.txt', 'w') as f:
        for info in kuchikomiinfolist:
            f.write(str(info) + '\n')
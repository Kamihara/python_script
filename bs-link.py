#!/usr/bin/python
# coding: utf-8

import sys
import time
import csv
from bs4 import BeautifulSoup
import urllib.request as req

# 店舗URLリストの取得
def get_shopurllist(url):
    res = req.urlopen(url)
    # time.sleep(3)
    soup2 = BeautifulSoup(res, "html.parser")
    shoplists = soup2.find_all("a", attrs={"class": "list-rst__rst-name-target"})
    shopurllists = []

    for shop in shoplists:
        shopurl = shop.attrs['href']
        shopurllists.append(shopurl)

    return shopurllists

# 店舗基本情報の取得
def get_shop_baseinfo(urllist):
    for url in urllist:
        res3 = req.urlopen(url)
        # time.sleep(3)
        soup3 = BeautifulSoup(res3, "html.parser")
        print(shopbaseinfo)
        shopbaseinfo = soup3.find_all("script", attrs={"type": "application/ld+json"})

# クチコミ情報の取得
def get_kuchikomilist(url):
    kuchikomiurl = url + "/dtlrvwlst/"
    res4 = req.urlopen(kuchikomiurl)
    # time.sleep(3)
    soup4 = BeautifulSoup(res4, "html.parser")
    shopbaseinfo = soup4.find_all("script", attrs={"type": "application/ld+json"})
    print(shopbaseinfo)

################################################################
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]
    urllist = []

    # 一覧ページの1ページ目
    #url = "https://tabelog.com/tokyo/A1315/A131501/R1644/rstLst/?vs=1&sa=%E5%A4%A7%E4%BA%95%E7%94%BA%E9%A7%85&sk=&lid=hd_search1&vac_net=&svd=20170601&svt=1900&svps=2&hfc=1&sw="
    url = "https://tabelog.com/tokyo/A1315/A131501/R1644/rstLst/?vs=1&sa=%E5%A4%A7%E4%BA%95%E7%94%BA%E9%A7%85&sk=&lid=hd_search1&vac_net=&svd=20170612&svt=2400&svps=2&hfc=1&sw="

    while(True):
        # 店舗URLリストの取得
        urllist.append(get_shopurllist(url))

        time.sleep(3)
        res = req.urlopen(url)
        # 次の20件へのリンクを取得
        soup = BeautifulSoup(res, "html.parser")
        ln = soup.find("a", attrs={"class": "page-move__target--next"})
        print(ln)
        if ln == None:
            # 最終ページに到達したら終了
            break
        else:
            url = ln.attrs['href']

    for page in urllist:
        for url in page:
            print(url)
            print(page)


    #with open('shopurllist.csv', 'w') as f:
    #    for listpage in shopurllist:
    #        for url in listpage:
    #            writer = csv.writer(f, lineterminator='\n')
    #            writer.writerow(url)



    # print(shopurllist)
    # get_shop_baseinfo(shopurllists)

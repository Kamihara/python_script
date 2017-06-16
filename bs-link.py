#!/usr/bin/python
# coding: utf-8

import sys
import time
import csv
from bs4 import BeautifulSoup
import urllib.request as req
from urllib.parse import urljoin

# 店舗URLリストの取得
def get_shopurllist(url):
    cnt = 0
    shopurllist = []
    while(True):
        # 一覧ページ内のurl20件を取得する
        res1 = req.urlopen(url)
        time.sleep(3)
        soup = BeautifulSoup(res1, "html.parser")
        shoplist = soup.find_all("a", attrs={"class": "list-rst__rst-name-target"})

        for shop in shoplist:
            shopurl = shop.attrs['href']
            shopurllist.append(shopurl)

        # 次の20件ページを取得する
        res2 = req.urlopen(url)
        # 次の20件へのリンクを取得
        soup2 = BeautifulSoup(res2, "html.parser")
        ln = soup2.find("a", attrs={"class": "page-move__target--next"})
        # 暫定で全3ページ分だけ取得
        cnt += 1
        if cnt >= 2:
            break
        # 暫定ここまで
        if ln == None:
            # 最終ページに到達したら終了
            break
        else:
            url = ln.attrs['href']

    return shopurllist

# 店舗基本情報の取得
def get_shop_baseinfo(urllist):
    shopinfolist = []
    for url in urllist:
        res = req.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        shopbaseinfo = soup.find_all("script", attrs={"type": "application/ld+json"})
        for info in shopbaseinfo:
            shopbaseinfo_json = info.string.strip()
        shopinfolist.append([url, shopbaseinfo_json])
    return shopinfolist

# クチコミ情報の取得
def get_kuchikomilist(url):
    while(True):
        res = req.urlopen(kuchikomipageurl)
        # time.sleep(3)
        soup = BeautifulSoup(res, "html.parser")
        kuchikomilists = soup.find_all("class", attrs={"type": "rvw-item__title-target"})

        print(kuchikomilists)
        return kuchikomilists
    #for k in kuchikomiurllists:
    #    kuchikomiurl = k.attrs['href']
    #    print(kuchikomiurl)
        #kuchikomiurllists.append(kuchikomiurl)


################################################################
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]
    urllist = []
    cnt = 0

    # 一覧ページの1ページ目
    url = "https://tabelog.com/tokyo/A1315/A131501/R1644/rstLst/?vs=1&sa=%E5%A4%A7%E4%BA%95%E7%94%BA%E9%A7%85&sk=&lid=hd_search1&vac_net=&svd=20170612&svt=2400&svps=2&hfc=1&sw="

    # 店舗URL全件取得
    shopurllist = get_shopurllist(url)

    # 店舗URLをファイルへ出力
    with open('shopurllist.txt', 'w') as f:
        for url in shopurllist:
            f.write(url + '\n')

    with open('shopurllist.csv', 'w') as c:
        csvwriter = csv.writer(c)
        csvwriter.writerow(shopurllist)

    # 店舗基本情報取得
    shopinfolist = get_shop_baseinfo(shopurllist)

    # 店舗基本情報をファイルへ出力
    with open('shopinfolist.txt', 'w') as f:
        for info in shopinfolist:
            f.write(str(info) + '\n')

    #with open('shopinfolist.csv', 'w') as c:
    #    csvwriter = csv.writer(c)
    #    csvwriter.writerow(shopinfolist)

    #for listpage in urllist:
    #    for url in listpage:
    #        shopbaseinfolist.append(get_shop_baseinfo(url))

    #shopreviewlist = []
    #for listpage in urllist:
    #    for url in listpage:
    #        while(True):
    #            kuchikomipageurl = urljoin(url, "/dtlrvwlst/")

    #            # 店舗URLリストの取得
    #            shopreviewlist.append(get_kuchikomilist(kuchikomipageurl))

    #            time.sleep(3)
    #            res = req.urlopen(url)
                # 次の20件へのリンクを取得
    #            soup = BeautifulSoup(res, "html.parser")
    #            ln = soup.find("a", attrs={"class": "page-move__target--next"})
    #            print(ln)
                # 暫定で全3ページ分だけ取得
    #            cnt += 1
    #            if cnt >= 2:
    #                break
                # 暫定ここまで
    #            if ln == None:
                    # 最終ページに到達したら終了
    #                break
    #            else:
    #                url = ln.attrs['href']


    # 店舗基本情報をファイルへ出力
    #with open('shopbaseinfolist.txt', 'w') as f:
    #    for shopbaseinfo in shopbaseinfolist:
    #        f.write(str(shopbaseinfo) + '\n')

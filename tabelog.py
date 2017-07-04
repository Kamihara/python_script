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
    cnt = 0
    shopurl_list = []
    while(True):
        # 一覧ページ内のurl20件を取得する
        res1 = req.urlopen(url)
        time.sleep(3)
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

# 店舗基本情報の取得
def get_shopbaseinfo(urllist):
    shopinfo_list = []
    for url in urllist:
        time.sleep(3)
        res = req.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        shopbaseinfo = soup.find("script", attrs={"type": "application/ld+json"})
        shopbaseinfo_json = shopbaseinfo.string.strip()
        shopinfo_list.append([url, shopbaseinfo_json])
        print(shopbaseinfo_json)
    return shopinfo_list

# クチコミURLリストの取得
def get_kuchikomiurl(url):
    cnt = 0
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

                time.sleep(3)
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


# クチコミ情報の取得
def get_kuchikomi_info(urllist):
    kuchikomiinfo_list = []
    with open('kuchikomiinfolist.csv', 'w') as c:
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
    # 一覧ページの1ページ目
    url = args[1]
    #url = "https://tabelog.com/tokyo/A1315/A131501/R1644/rstLst/?vs=1&sa=%E5%A4%A7%E4%BA%95%E7%94%BA%E9%A7%85&sk=&lid=hd_search1&vac_net=&svd=20170612&svt=2400&svps=2&hfc=1&sw="

    # 店舗URL全件取得
    shopurllist = get_shopurl_list(url)

    # 店舗URLをファイルへ出力
    with open('shopurllist.txt', 'w') as f:
        for url in shopurllist:
            f.write(url + '\n')

    with open('shopurllist.csv', 'w') as c:
        csvwriter = csv.writer(c)
        csvwriter.writerow(shopurllist)

    # 店舗基本情報取得
    shopinfolist = get_shopbaseinfo(shopurllist)

    # 店舗基本情報をファイルへ出力
    with open('shopinfolist.txt', 'w') as f:
        for info in shopinfolist:
            f.write(str(info) + '\n')

    # 店舗クチコミURL全件取得
    kuchikomiurllist = get_kuchikomiurl(shopurllist)


    # 店舗クチコミ情報取得
    kuchikomiinfolist = get_kuchikomi_info(kuchikomiurllist)

    # 店舗クチコミ情報をファイルへ出力
    with open('kuchikomiinfolist.txt', 'w') as f:
        for info in kuchikomiinfolist:
            f.write(str(info) + '\n')
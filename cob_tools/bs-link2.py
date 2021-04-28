#!/usr/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib.request as req
import csv

url = "https://tabelog.com/tokyo/A1315/A131501/R1644/rstLst/?vs=1&sa=%E5%A4%A7%E4%BA%95%E7%94%BA%E9%A7%85&sk=&lid=hd_search1&vac_net=&svd=20170601&svt=1900&svps=2&hfc=1&sw="
urllist = [url]

with open('urllist.csv', 'wt') as f:
    CsvFile = csv.reader(open('urllist.csv'),delimiter='\n')
    while(True):
        res = req.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        ln = soup.find("a", attrs={"class": "page-move__target--next"})
        if ln == None:
            break
        else:
            newurl = ln.attrs['href']
            writer.writerows(newurl)
            url = newurl




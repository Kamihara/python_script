#!/usr/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://tabelog.com/tokyo/A1315/A131501/R1644/rstLst/?vs=1&sa=%E5%A4%A7%E4%BA%95%E7%94%BA%E9%A7%85&sk=&lid=hd_search1&vac_net=&svd=20170601&svt=1900&svps=2&hfc=1&sw="

while(True):
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    ln = soup.find_all("a", attrs={"class": "page-move__target--next"})
    if ln == "":
        exit()
    else:
        print(ln)
    url = ln

import requests
import time
from bs4 import BeautifulSoup


class TabelogKuchikomiHtmlGetter:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "lxml")

    def get_name(self):
        return self.__get_text(".display-name")

    def get_tel(self):
        return self.__get_text(".rstinfo-table__tel-num")

    def get_address(self):
        elements = self.soup.select(".rstinfo-table__address span")
        if not elements:
            return None

        return "".join([elm.get_text().strip() for elm in elements])

    def __get_text(self, selector):
        elements = self.soup.select(selector)
        if not elements:
            return None

        element = elements[0]
        return element.get_text().strip()


def get_html(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":

    shop_urls = list(open("kuchikomiurllist.txt"))
    for url in shop_urls:
        print(url)
        html = get_html(url)
        f = open("kuchikomi/{0}.html".format(url.split('/')[-2]), "w")
        f.write(html)
        time.sleep(1)
    # html = get_html("https://tabelog.com/tokyo/A1315/A131501/13196426/")
    # f = open("tabelog.html", "w")
    # f.write(html)
    # html = open("tabelog.html").read()

    # data = TabelogDataGetter(html)
    # print(data.get_name())
    # print(data.get_tel())
    # print(data.get_address())

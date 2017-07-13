import requests
import time
from bs4 import BeautifulSoup


class TabelogHtmlGetter:
    def __init__(self, html):
        h = open(html).read()
        self.soup = BeautifulSoup(h, "lxml")

    def get_name(self):
        return self.__get_text(".display-name")

    def get_tel(self):
        return self.__get_text(".rstinfo-table__tel-num")

    def get_address(self):
        elements = self.soup.select(".rstinfo-table__address span")
        if not elements:
            return None

        return "".join([elm.get_text().strip() for elm in elements])

    def get_rstinfo(self):
        return self.__get_text("rstinfo-table__table")

    def get_genre(self):
        return self.__get_text("")

    def get_open_time(self):
        return self.__get_text("")

    def get_holiday(self):
        return self.__get_text("")

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

    shop_urls = list(open("shopurllist.txt"))
    for url in shop_urls:
        print(url)
        html = get_html(url)
        f = open("shops/{0}.html".format(url.split('/')[-2]), "w")
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

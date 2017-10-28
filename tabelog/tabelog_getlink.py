from bs4 import BeautifulSoup
import csv
import sys
import glob
import time
import os


class linkGetter:
    def __init__(self, html):
        h = open(html).read()
        self.soup = BeautifulSoup(h, "lxml")

    def get_name(self):
        return self.__get_text(".display-name")

    def get_link(self):
        elements = self.soup.select(".display-name > a")
        return elements[0].attrs['href']

    def __get_text(self, selector):
        elements = self.soup.select(selector)
        if not elements:
            return None

        element = elements[0]
        return element.get_text().strip()


if __name__ == "__main__":

    args = sys.argv
    dir = "/Users/YoshitoKamihara/development/python_script/tabelog/ooimachi/shops"
    html_list = glob.glob(dir + '/*')

    for h in html_list:
        print(h)

        link_list = []
        html = linkGetter(h)

        # shop_name varchar(255) null, -- 店名
        shop_name = html.get_name()
        link_list.append(shop_name)

        # link
        link = html.get_link()
        link_list.append(link)
        print(link_list)

        sql = "update oaiso_shop_test set links = \"" + link_list[1] + \
              "\" where shop_name = " + "\"" + link_list[0] + "\";\n"

        # sql = "update tabelog_shop_info set URL = \"" + link_list[1] + \
        #       "\" where shop_name = " + "\"" + link_list[0] + "\";\n"

        print(sql)
        f = open('./ooimachi/oaiso_shop_test_links_update.sql', 'a')
        # f = open('./ooimachi/link_update.sql', 'a')
        f.write(sql)

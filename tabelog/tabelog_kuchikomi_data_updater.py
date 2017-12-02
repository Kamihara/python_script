from bs4 import BeautifulSoup
import glob
import csv
import sys
import json

class TabelogDataGetter:
    def __init__(self, html):
        h = open(html).read()
        self.soup = BeautifulSoup(h, "lxml")

    def get_name(self):
        return self.__get_text(".display-name")

    def get_tel(self):
        return self.__get_text(".rstdtl-side-yoyaku__tel-number")

    def get_address(self):
        elements = self.soup.select(".rstinfo-table__address span")
        if not elements:
            return None

        return "".join([elm.get_text().strip() for elm in elements])

    def get_URL(self):
        elements = self.soup.select(".display-name > a")
        return elements[0].attrs['href']

    def get_shop_score(self):
        return self.__get_text(".rdheader-rating__score-val-dtl")

    def get_shop_dinner_score(self):
        return self.__get_text(".rdheader-rating__time-icon--dinner").replace('夜の点数：','')

    def get_shop_lunch_score(self):
        return self.__get_text(".rdheader-rating__time-icon--lunch").replace('昼の点数：','')

    def get_latitude(self):
        j = self.soup.find("script", attrs={"type": "application/ld+json"})
        json_str = j.get_text().strip()
        json_dict = json.loads(json_str)
        return json_dict['geo']['latitude']

    def get_longitude(self):
        j = self.soup.find("script", attrs={"type": "application/ld+json"})
        json_str = j.get_text().strip()
        json_dict = json.loads(json_str)
        return json_dict['geo']['longitude']

    def get_rstinfo(self, search_word):

        # 基本情報のテーブルを取得
        info_table = self.soup.find_all("table", attrs={"class": "rstinfo-table__table"})

        # テーブルから各行trタグを集める
        for t in info_table:
            tr_all = t.find_all('tr')

            # 検索ワードを含む見出しthタグがあればそのデータを返す
            for tr in tr_all:
                th = tr.find('th').get_text()

                if search_word == th:
                    val = tr.find('td').get_text()
                    return val.replace('\n', '').replace(' ', '').replace('\t', '')
                else:
                    continue

        # 全行チェックしても見つからなければno data
        return "no data"

    def __get_text(self, selector):
        elements = self.soup.select(selector)
        if not elements:
            return None

        element = elements[0]
        return element.get_text().strip()


if __name__ == "__main__":

    args = sys.argv
    dir = args[1]
    kuchikomi_info = dir + '/kuchikomi_info.csv'

    with open(kuchikomi_info, 'r') as c:
        f = open(dir + '/tabelog_kuchikomi_info_update.sql', 'w')
        cr = csv.reader(c, delimiter='\t')

        for row in cr:
            sql = "update tabelog_shop_review set shopURL = " + "\'" + row[24] + "\'" \
                    ", reviewURL = " + "\'" + row[25] + "\'" \
                    " where shop_name = " + "\'" + row[0] + "\' " \
                    " and kuchikomi_title = " + "\'" + row[1] + "\' " ";\n"

            print(sql)
            f.write(sql)

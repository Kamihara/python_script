from bs4 import BeautifulSoup
import glob
import csv
import sys

class TabelogDataGetter:
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

    def get_shop_score(self):
        return self.__get_text(".rdheader-rating__score-val")

    def get_shop_dinner_score(self):
        elements = self.soup.select(".rdheader-rating__time-icon--dinner em")
        if not elements:
            return 0

        return elements[0].get_text()

    def get_shop_lunch_score(self):
        elements = self.soup.select(".rdheader-rating__time-icon--lunch em")
        if elements[0].get_text() == "-":
            return 0

        return elements[0].get_text()

    def get_rstinfo_titles(self):
        titles = []
        tables = self.soup.find_all("table", attrs={"class": "rstinfo-table__table"})

        for table in tables:
            columns = table.find_all('th')
            for col in columns:
                titles.append(col.get_text().replace('\n', '').replace(' ', ''))

        return titles

    def get_rstinfo(self, column):
        row = []
        tables = self.soup.find_all("table", attrs={"class": "rstinfo-table__table"})

        for col in column:
            flg_hit = False

            for table in tables:
                tr_all = table.find_all('tr')

                for tr in tr_all:
                    th = tr.find('th').get_text()

                    if col == th:
                        row.append(tr.find('td').get_text().replace('\n', '').replace(' ', ''))
                        flg_hit = True
                    else:
                        continue

            if flg_hit == False:
                row.append("no data")

        return row

    def __get_text(self, selector):
        elements = self.soup.select(selector)
        if not elements:
            return None

        element = elements[0]
        return element.get_text().strip()


if __name__ == "__main__":
    args = sys.argv
    dir = args[1]
    html_list = glob.glob(dir + '/shops/*')
    header = []
    rows = []

    # 基本情報エリアから取得したい情報を指定する
    for h in html_list:
        html = TabelogDataGetter(h)
        titles = html.get_rstinfo_titles()
        print(h)
        for t in titles:
            if t not in header:
                header.append(t)

    header.append("shop_score")
    header.append("shop_dinner_score")
    header.append("shop_lunch_score")

    with open(dir + '/shop_info_title.csv', 'a') as c:
        cw = csv.writer(c, delimiter='\t')
        cw.writerow(header)

    for h in html_list:
        html = TabelogDataGetter(h)
        row = []
        print(h)
        with open(dir + '/shop_info.csv', 'a') as c:
            cw = csv.writer(c, delimiter='\t')
            row = html.get_rstinfo(header)
            row.append(html.get_shop_score())
            row.append(html.get_shop_dinner_score())
            row.append(html.get_shop_lunch_score())
            cw.writerow(row)

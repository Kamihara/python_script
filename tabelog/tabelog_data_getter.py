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
    uniq_col = []
    rows = []

    for h in html_list:
        html = TabelogDataGetter(h)
        titles = html.get_rstinfo_titles()
        for t in titles:
            if t not in uniq_col:
                uniq_col.append(t)

    with open(dir + '/shop_info_title.csv', 'a') as c:
        cw = csv.writer(c, delimiter='\t')
        cw.writerow(uniq_col)

    for h in html_list:
        html = TabelogDataGetter(h)
        with open(dir + '/shop_info.csv', 'a') as c:
            cw = csv.writer(c, delimiter='\t')
            cw.writerow(html.get_rstinfo(uniq_col))

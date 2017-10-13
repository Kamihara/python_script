import requests
from bs4 import BeautifulSoup
import glob
import csv
import sys


class TabelogKuchikomiDataGetter:
    def __init__(self, html):
        h = open(html).read()
        self.soup = BeautifulSoup(h, "lxml")

    def get_name(self):
        return self.__get_text(".display-name")

    def get_kuchikomi_title(self):
        try:
            return self.__get_text(".rvw-item__title")
        except:
            return "no data"

    def get_kuchikomi_text(self):
        text = self.__get_text(".rvw-item__rvw-comment")
        return text.replace('\\', '￥')

    def get_kuchikomi_img(self):
        img_url = []
        review_imgs = self.soup.find_all("div", attrs={"class": "rvw-photo__list-img"})
        for i in review_imgs:
            img_url.append(i.find("a").attrs['href'])
        return img_url

    def get_shop_score(self):
        return self.__get_text(".rdheader-rating__score-val")

    def get_shop_dinner_score(self):
        return self.__get_text(".rdheader-rating__time-icon--dinner").replace('夜の点数：','')

    def get_shop_lunch_score(self):
        return self.__get_text(".rdheader-rating__time-icon--lunch").replace('昼の点数：','')

    def get_personal_dinner_score(self):
        exist_check = self.soup.select(".rvw-item__ratings-item")

        for c in exist_check:
            if c.select(".c-rating__time--dinner"):
                return c.select(".c-rating__val")[0].get_text()

        return('-')

    def get_personal_lunch_score(self):
        exist_check = self.soup.select(".rvw-item__single-ratings-item")

        for c in exist_check:
            if c.select(".c-rating__time--lunch"):
                return c.select(".c-rating__val")[0].get_text()

        return('-')


    def get_personal_dinner_detail_score(self):
        exist_check = self.soup.select(".rvw-item__single-ratings-item")

        for c in exist_check:
            if c.select(".c-rating__time--dinner"):
                details = c.select(".rvw-item__single-ratings-dtlscore-score")
                taste_rate = details[0].get_text()
                service_rate = details[1].get_text()
                atmosphere_rate = details[2].get_text()
                cp_rate = details[3].get_text()
                drink_rate = details[4].get_text()
                return [taste_rate, service_rate, atmosphere_rate, cp_rate, drink_rate]

        return ['-', '-', '-', '-', '-']

    def get_personal_lunch_detail_score(self):
        exist_check = self.soup.select(".rvw-item__single-ratings-item")

        for c in exist_check:
            if c.select(".c-rating__time--lunch"):
                details = c.select(".rvw-item__single-ratings-dtlscore-score")
                taste_rate = details[0].get_text()
                service_rate = details[1].get_text()
                atmosphere_rate = details[2].get_text()
                cp_rate = details[3].get_text()
                drink_rate = details[4].get_text()
                return [taste_rate, service_rate, atmosphere_rate, cp_rate, drink_rate]

        return ['-', '-', '-', '-', '-']

    def get_reviewer(self):
        r = self.soup.select(".other-rvws__rvwr-name")
        try:
            return str(r[0].find("span")).split("span")[1].replace(">","").replace("<","")
        except:
            return "no data"

    def get_follower_count(self):
        try:
            return self.__get_text(".other-rvws__rvwr-name-count").replace('）さんの他のお店の口コミ','').replace('（','')
        except:
            return 0

    def __get_text(self, selector):
        elements = self.soup.select(selector)
        if not elements:
            return None

        element = elements[0]
        return element.get_text().strip().replace('\n','')

if __name__ == "__main__":

    args = sys.argv
    dir = args[1]
    html_list = glob.glob(dir + '/kuchikomi/*')

    with open(dir + '/kuchikomi_info.csv', 'a') as c:
        cw = csv.writer(c, delimiter='\t')
        header = ['shop_name',
                  'kuchikomi_title',
                  'kuchikomi_text',
                  'kuchikomi_img_list',
                  'shop_score',
                  'shop_lunch_score',
                  'shop_dinner_score',
                  'personal_lunch_score',
                  'personal_dinner_score',
                  'personal_lunch_taste_rate',
                  'personal_lunch_service_rate',
                  'personal_lunch_atmosphere_rate',
                  'personal_lunch_cp_rate',
                  'personal_lunch_drink_rate',
                  'personal_dinner_taste_rate',
                  'personal_dinner_service_rate',
                  'personal_dinner_atmosphere_rate',
                  'personal_dinner_cp_rate',
                  'personal_dinner_drink_rate',
                  'reviewer',
                  'follower_count']
        cw.writerow(header)

        for h in html_list:
            l = []
            html = TabelogKuchikomiDataGetter(h)
            print(h)

            shop_name = html.get_name()
            l.append(shop_name)

            kuchikomi_title = html.get_kuchikomi_title()
            l.append(kuchikomi_title)

            kuchikomi_text = html.get_kuchikomi_text()
            l.append(kuchikomi_text)

            kuchikomi_img_list = html.get_kuchikomi_img()
            l.append(kuchikomi_img_list)

            shop_score = html.get_shop_score()
            l.append(shop_score.replace('-', None))

            shop_lunch_score = html.get_shop_lunch_score()
            l.append(shop_lunch_score.replace('-', None))

            shop_dinner_score = html.get_shop_dinner_score()
            l.append(shop_dinner_score.replace('-', None))

            personal_lunch_score = html.get_personal_lunch_score()
            l.append(personal_lunch_score.replace('-', None))

            personal_dinner_score = html.get_personal_dinner_score()
            l.append(personal_dinner_score.replace('-', None))

            personal_lunch_detail_score_list = html.get_personal_lunch_detail_score()
            for score in personal_lunch_detail_score_list:
                l.append(score.replace('-', None))

            personal_dinner_detail_score_list = html.get_personal_dinner_detail_score()
            for score in personal_dinner_detail_score_list:
                l.append(score.replace('-', None))

            reviewer = html.get_reviewer()
            l.append(reviewer)

            follower_count = html.get_follower_count()
            l.append(follower_count)

            print(l)

            cw.writerow(l)

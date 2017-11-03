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

    def get_URL(self):
        elements = self.soup.select(".display-name > a")
        return elements[0].attrs['href']

    # def get_shop_score(self):
    #     return self.__get_text(".rdheader-rating__score-val")
    #
    # def get_shop_dinner_score(self):
    #     elements = self.soup.select(".rdheader-rating__time-icon--dinner em")
    #     if not elements:
    #         return 0
    #
    #     return elements[0].get_text()
    #
    # def get_shop_lunch_score(self):
    #     elements = self.soup.select(".rdheader-rating__time-icon--lunch em")
    #     if elements[0].get_text() == "-":
    #         return 0
    #
    #     return elements[0].get_text()
    #
    # def get_rstinfo_titles(self):
    #     titles = []
    #     tables = self.soup.find_all("table", attrs={"class": "rstinfo-table__table"})
    #
    #     for table in tables:
    #         columns = table.find_all('th')
    #         for col in columns:
    #             titles.append(col.get_text().replace('\n', '').replace(' ', ''))
    #
    #     return titles

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
    html_list = glob.glob(dir + '/shops/*')

    # # 基本情報エリアから取得したい情報を指定する
    # for h in html_list:
    #     html = TabelogDataGetter(h)
    #     titles = html.get_rstinfo_titles()
    #     print(h)
    #     for t in titles:
    #         if t not in header:
    #             header.append(t)
    #
    # header.append("shop_score")
    # header.append("shop_dinner_score")
    # header.append("shop_lunch_score")

    # with open(dir + '/shop_info_title.csv', 'a') as c:
    #     cw = csv.writer(c, delimiter='\t')
    #     cw.writerow(header)

    with open(dir + '/shop_info.csv', 'a') as c:
        cw = csv.writer(c, delimiter='\t')

        for h in html_list:
            l = []
            html = TabelogDataGetter(h)
            print(h)

            # shop_name varchar(255) null, -- 店名
            shop_name = html.get_name()
            l.append(shop_name)

            # genre varchar(255) null, -- ジャンル
            genre = html.get_rstinfo("ジャンル")
            l.append(genre)

            # reservation varchar(255) null, -- 予約
            reservation = html.get_rstinfo("予約・お問い合わせ")
            l.append(reservation)

            # reservation_availability varchar(255) null, -- 予約可否
            reservation_availability = html.get_rstinfo("予約可否")
            l.append(reservation_availability)

            # address varchar(255) null, -- 住所
            address = html.get_rstinfo("住所")
            l.append(address.replace("大きな地図を見る周辺のお店を探す", ""))

            # transportation varchar(255) null, -- 交通手段
            transportation = html.get_rstinfo("交通手段")
            l.append(transportation)

            # bussiness_hours varchar(255) null, -- 営業時間
            bussiness_hours = html.get_rstinfo("営業時間")
            l.append(bussiness_hours)

            # regular_holiday varchar(255) null, -- 定休日
            regular_holiday = html.get_rstinfo("定休日")
            l.append(regular_holiday)

            # budget_from_user varchar(255) null, -- 予算（ユーザ）
            # budget_from_user = html.get_rstinfo("予算（ユーザーより）")
            budget_from_user = html.get_rstinfo("予算（口コミ集計）")
            l.append(budget_from_user.replace("予算分布を見る", ""))

            # budget_from_user_night_min int null, -- 予算（ユーザ）
            l.append("")
            # budget_from_user_night_max int null, -- 予算（ユーザ）
            l.append("")
            # budget_from_user_lunch_min int null, -- 予算（ユーザ）
            l.append("")
            # budget_from_user_lunch_max int null, -- 予算（ユーザ）
            l.append("")

            # budget_from_shop varchar(255) null, -- 予算（店舗）
            budget_from_shop = html.get_rstinfo("予算")
            l.append(budget_from_shop.replace("予算分布を見る", ""))

            # budget_from_shop_night_min int null, -- 予算（店舗）
            l.append("")
            # budget_from_shop_night_max int null, -- 予算（店舗）
            l.append("")
            # budget_from_shop_lunch_min int null, -- 予算（店舗）
            l.append("")
            # budget_from_shop_lunch_max int null, -- 予算（店舗）
            l.append("")

            # card varchar(255) null, -- カード
            card = html.get_rstinfo("カード")
            l.append(card)

            # capacity varchar(255) null, -- 席数
            capacity = html.get_rstinfo("席数")
            l.append(capacity)

            # capacity_number int null, -- 席数
            l.append("")

            # private_room varchar(255) null, -- 個室
            private_room = html.get_rstinfo("個室")
            l.append(private_room)

            # parking varchar(255) null, -- 駐車場
            parking = html.get_rstinfo("駐車場")
            l.append(parking)

            # facility varchar(255) null, -- 設備
            facility = html.get_rstinfo("空間・設備")
            l.append(facility)

            # mobile_phone varchar(255) null, -- 携帯
            mobile_phone = html.get_rstinfo("携帯電話")
            l.append(mobile_phone)

            # scene varchar(255) null, -- 利用シーン
            scene = html.get_rstinfo("利用シーン")
            l.append(scene.replace("こんな時によく使われます。", ""))

            # service varchar(255) null, -- サービス
            service = html.get_rstinfo("サービス")
            l.append(service)

            # `1st_poster` varchar(255) null, -- 初投稿者
            first_poster = html.get_rstinfo("初投稿者")
            l.append(first_poster)

            # last_poster varchar(255) null, -- 最終投稿者
            last_poster = html.get_rstinfo("最近の編集者")
            l.append(last_poster)

            # reserved varchar(255) null, -- 貸し切り
            reserved = html.get_rstinfo("貸切")
            l.append(reserved)

            # smoking varchar(255) null, -- 喫煙
            smoking = html.get_rstinfo("禁煙・喫煙")
            l.append(smoking)

            # drinking varchar(255) null, -- 飲み物
            drinking = html.get_rstinfo("ドリンク")
            l.append(drinking)

            # cuisine varchar(255) null, -- 料理
            cuisine = html.get_rstinfo("料理")
            l.append(cuisine)

            # location varchar(255) null, -- 場所
            location = html.get_rstinfo("ロケーション")
            l.append(location)

            # HP varchar(255) null, -- ホームページ
            HP = html.get_rstinfo("ホームページ")
            l.append(HP)

            # official_account varchar(255) null, -- 公式アカウント
            official_account = html.get_rstinfo("公式アカウント")
            l.append(official_account)

            # opening_date varchar(255) null, -- 開店日
            opening_date = html.get_rstinfo("オープン日")
            l.append(opening_date)

            # contact varchar(255) null, -- 連絡先
            contact = html.get_rstinfo("お問い合わせ")
            l.append(contact)

            # remark varchar(255) null, -- 備考
            remark = html.get_rstinfo("備考")
            l.append(remark)

            # child_accompanied varchar(255) null, -- 子供連れ
            child_accompanied = html.get_rstinfo("お子様同伴")
            l.append(child_accompanied)

            # charge varchar(255) null, -- チャージ料
            charge = html.get_rstinfo("サービス料・チャージ")
            l.append(charge)

            # course varchar(255) null, -- コース
            course = html.get_rstinfo("コース")
            l.append(course)

            # free_drink_course varchar(255) null, -- 飲み放題
            free_drink_course = html.get_rstinfo("飲み放題コース")
            l.append(free_drink_course)

            # related_store varchar(255) null, -- 関連店舗
            related_store = html.get_rstinfo("関連店舗情報")
            l.append(related_store)

            # link varchar(255) null, -- リンク
            link = html.get_rstinfo("その他リンク")
            l.append(link)

            # tel varchar(255) null, -- 電話番号
            tel = html.get_rstinfo("電話番号")
            l.append(tel)

            # dress_code varchar(255) null, -- ドレスコード
            dress_code = html.get_rstinfo("ドレスコード")
            l.append(dress_code)

            # id  int(11) -- id
            id = 0
            l.append(id)

            # latitude
            l.append("")

            # longtitude
            l.append("")

            # genre_oaiso
            l.append("")

            # URL
            URL = html.get_URL()
            l.append(URL)

            cw.writerow(l)

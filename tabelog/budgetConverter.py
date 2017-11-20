import csv
import sys
import time
import os

if __name__ == "__main__":

    args = sys.argv
    data = []

    # with open('/Users/YoshitoKamihara/Documents/aiit/PBL/dev/analysis/shop_analysis_budget.tsv', 'r') as t:
    with open('/Users/YoshitoKamihara/Documents/aiit/PBL/dev/analysis/shop_analysis_budget_20171106.tsv', 'r') as t:
        cr = csv.reader(t, delimiter='\t')
        for row in cr:
            dict = {"budget_from_shop_night_min": "null",
                    "budget_from_shop_night_max": "null",
                    "budget_from_shop_lunch_min": "null",
                    "budget_from_shop_lunch_max": "null",
                    "budget_from_user_night_min": "null",
                    "budget_from_user_night_max": "null",
                    "budget_from_user_lunch_min": "null",
                    "budget_from_user_lunch_max": "null",
                    "id": 0}

            # 店舗予算
            if row[0] == "no data":
                dict["budget_from_shop_night_min"] = "null"
                dict["budget_from_shop_night_max"] = "null"
                dict["budget_from_shop_lunch_min"] = "null"
                dict["budget_from_shop_lunch_max"] = "null"
            else:
                cols = row[0].split('[')
                if cols[1][0:2] == "夜]":
                    # col = cols[1].split('〜')
                    col = cols[1].split('～')
                    # print(col[0])
                    # print(col[1])
                    try:
                        dict["budget_from_shop_night_min"] = int(
                            col[0].replace("夜]", "").replace("￥", "").replace(",", ""))
                    except:
                        dict["budget_from_shop_night_min"] = "null"
                    try:
                        dict["budget_from_shop_night_max"] = int(
                            col[1].replace("夜]", "").replace("￥", "").replace(",", ""))
                    except:
                        dict["budget_from_shop_night_max"] = "null"


                elif cols[1][0:2] == "昼]":
                    # col = cols[1].split('〜')
                    col = cols[1].split('～')
                    try:
                        dict["budget_from_shop_lunch_min"] = int(
                            col[0].replace("昼]", "").replace("￥", "").replace(",", ""))
                    except:
                        dict["budget_from_shop_lunch_min"] = "null"
                    try:
                        dict["budget_from_shop_lunch_max"] = int(
                            col[1].replace("昼]", "").replace("￥", "").replace(",", ""))
                    except:
                        dict["budget_from_shop_lunch_max"] = "null"
                try:
                    if cols[2][0:2] == "夜]":
                        # col = cols[1].split('〜')
                        col = cols[2].split('～')
                        # print(col[0])
                        # print(col[1])
                        try:
                            dict["budget_from_shop_night_min"] = int(
                                col[0].replace("夜]", "").replace("￥", "").replace(",", ""))
                        except:
                            dict["budget_from_shop_night_min"] = "null"
                        try:
                            dict["budget_from_shop_night_max"] = int(
                                col[1].replace("夜]", "").replace("￥", "").replace(",", ""))
                        except:
                            dict["budget_from_shop_night_max"] = "null"
                    elif cols[2][0:2] == "昼]":
                        # col = cols[1].split('〜')
                        col = cols[2].split('～')
                        try:
                            dict["budget_from_shop_lunch_min"] = int(
                                col[0].replace("昼]", "").replace("￥", "").replace(",", ""))
                        except:
                            dict["budget_from_shop_lunch_min"] = "null"
                        try:
                            dict["budget_from_shop_lunch_max"] = int(
                                col[1].replace("昼]", "").replace("￥", "").replace(",", ""))
                        except:
                            dict["budget_from_shop_lunch_max"] = "null"
                except:
                    pass

            # ユーザ予算
            if row[1] == '':
                dict["budget_from_user_night_min"] = "null"
                dict["budget_from_user_night_max"] = "null"
                dict["budget_from_user_lunch_min"] = "null"
                dict["budget_from_user_lunch_max"] = "null"
            else:
                cols = row[1].split('[')
                if cols[1][0:2] == "夜]":
                    # col = cols[1].split('〜')
                    col = cols[1].split('～')
                    print(col[0])
                    print(col[1])

                    try:
                        dict["budget_from_user_night_min"] = int(
                            col[0].replace("夜]", "").replace("￥", "").replace(",", ""))
                    except:
                        dict["budget_from_user_night_min"] = "null"
                    try:
                        dict["budget_from_user_night_max"] = int(
                            col[1].replace("夜]", "").replace("￥", "").replace(",", ""))
                    except:
                        dict["budget_from_user_night_max"] = "null"
                elif cols[1][0:2] == "昼]":
                    # col = cols[1].split('〜')
                    col = cols[1].split('～')

                    try:
                        dict["budget_from_user_lunch_min"] = int(
                            col[0].replace("昼]", "").replace("￥", "").replace(",", ""))
                    except:
                        dict["budget_from_user_lunch_min"] = "null"
                    try:
                        dict["budget_from_user_lunch_max"] = int(
                            col[1].replace("昼]", "").replace("￥", "").replace(",", ""))
                    except:
                        dict["budget_from_user_lunch_max"] = "null"
                try:
                    if cols[2][0:2] == "夜]":
                        # col = cols[1].split('〜')
                        col = cols[2].split('～')
                        print(col[0])
                        print(col[1])

                        try:
                            dict["budget_from_user_night_min"] = int(
                                col[0].replace("夜]", "").replace("￥", "").replace(",", ""))
                        except:
                            dict["budget_from_user_night_min"] = "null"
                        try:
                            dict["budget_from_user_night_max"] = int(
                                col[1].replace("夜]", "").replace("￥", "").replace(",", ""))
                        except:
                            dict["budget_from_user_night_max"] = "null"
                    elif cols[2][0:2] == "昼]":
                        # col = cols[1].split('〜')
                        col = cols[2].split('～')

                        try:
                            dict["budget_from_user_lunch_min"] = int(
                                col[0].replace("昼]", "").replace("￥", "").replace(",", ""))
                        except:
                            dict["budget_from_user_lunch_min"] = "null"
                        try:
                            dict["budget_from_user_lunch_max"] = int(
                                col[1].replace("昼]", "").replace("￥", "").replace(",", ""))
                        except:
                            dict["budget_from_user_lunch_max"] = "null"
                except:
                    pass

            dict["id"] = row[2]

            if dict["budget_from_shop_night_min"] == 30000:
                dict["budget_from_shop_night_max"] = 99999

            if dict["budget_from_shop_night_max"] == 999:
                dict["budget_from_shop_night_min"] = 0

            if dict["budget_from_shop_lunch_min"] == 30000:
                dict["budget_from_shop_lunch_max"] = 99999

            if dict["budget_from_shop_lunch_max"] == 999:
                dict["budget_from_shop_lunch_min"] = 0

            if dict["budget_from_user_night_min"] == 30000:
                dict["budget_from_user_night_max"] = 99999

            if dict["budget_from_user_night_max"] == 999:
                dict["budget_from_user_night_min"] = 0

            if dict["budget_from_user_lunch_min"] == 30000:
                dict["budget_from_user_lunch_max"] = 99999

            if dict["budget_from_user_lunch_max"] == 999:
                dict["budget_from_user_lunch_min"] = 0


            data.append(dict)

            # time.sleep(1)

    header = data[0].keys()

    with open('./budgetConvert_20171106.tsv', 'a') as t:
        cw = csv.DictWriter(t, header, delimiter='\t')
        header_row = {k: k for k in header}
        cw.writerow(header_row)

        for row in data:
            cw.writerow(row)

    with open('./budgetConvert_20171106.tsv', 'r') as t:
        cr = csv.reader(t, delimiter='\t')
        for row in cr:
            sql = "update tabelog_shop_info set budget_from_shop_night_min = " + row[0] + \
                  ", budget_from_shop_night_max = " + row[1] + \
                  ", budget_from_shop_lunch_min = " + row[2] + \
                  ", budget_from_shop_lunch_max = " + row[3] + \
                  ", budget_from_user_night_min = " + row[4] + \
                  ", budget_from_user_night_max = " + row[5] + \
                  ", budget_from_user_lunch_min = " + row[6] + \
                  ", budget_from_user_lunch_max = " + row[7] + \
                  " where id = " + row[8] + ";\n"

            print(sql)
            f = open('./budgetConvert_20171106.sql', 'a')
            f.write(sql)

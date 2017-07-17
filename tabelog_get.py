import glob
from tabelog_html_getter import TabelogHtmlGetter
import pandas as pd
import csv

if __name__ == "__main__":

    html_list = glob.glob('shops/*')

    for h in html_list:
        html = TabelogHtmlGetter(h)
        with open('shops/shop_info.csv', 'a') as c:
            cw = csv.writer(c, delimiter='\t')
            cw.writerow(html.get_rstinfo())
        # print(html.get_rstinfo())
        # data = pd.DataFrame(html.get_rstinfo())
        # data.to_csv('shop_info.csv', sep='\t')
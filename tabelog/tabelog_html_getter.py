import requests
import time
import csv
import sys


def get_html(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    args = sys.argv
    dir = args[1]
    with open(dir + "/shopurl_list.csv", "r") as c:
        cr = csv.reader(c)
        for c in cr:
            for url in c:
                print(url)
                html = get_html(url)
                f = open(dir + "/shops/{0}.html".format(url.split('/')[-2]), "w")
                f.write(html)
                time.sleep(30)

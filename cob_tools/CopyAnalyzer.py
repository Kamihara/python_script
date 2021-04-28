# coding: UTF-8
#!/usr/bin/python
import sys
import os
import glob
import csv
import time

class CopyAnalyzer:
    def __init__(self, path):
        self.path = path                        # /export/home/bp/cobol/copy/SAMPLE.cbl

    def basename(self):
        return os.path.basename(self.path)      # SAMPLE.cbl

    def name(self):
        return self.basename().split('.')[0]    # SAMPLE


    def search_using_src(self):
        ### 開発機向け
        # 該当コピー句が使用されているsrcを検索し、
        # srcのフルパスをリスト形式で返却する。

        result = []     

        # 調査対象srcライブラリ
        src_lib = []
        src_lib.append("/export/home/bp/cobol/main/src")
        src_lib.append("/export/home/bp/cobol/main/esrc")
        src_lib.append("/export/home/bp/cobol/sub/src")

        for lib in src_lib:
            src_list = glob.glob(lib + "/*")
            for src in src_list:
                with open(src, "r") as s:
                    for line in s.readlines():
                        cp = line.split()
                        #time.sleep(1)
                        try:
                            if cp[2].replace('.', '') == self.name():
                                print(line)
                                result.append(src)
                        except Exception as e:
                            print(e)

        return result

        
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    script_name = args[0]

    # arguments check
    if num != 2:
        print "Usage: %s filepath" % script_name
        quit()

    in_filepath = args[1]

    f = open(in_filepath, "r")
    lines = f.readlines()
    f.close()

    for copy_path in lines:
        copy = CopyAnalyzer(copy_path)

        l = []
        l.append(copy_path)

        with open("/BP/UNY020/" + script_name[:-3] + "_s1yst.out", "a") as o:
            for c in copy.search_using_src():
                l.append(c)

            cw = csv.writer(o, delimiter="\t")
            cw.writerow(l)

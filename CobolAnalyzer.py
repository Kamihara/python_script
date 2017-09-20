# coding: UTF-8
#!/usr/bin/python
import sys
import os
import glob
import csv

class CobolAnalyzer:
    def __init__(self, path):
        self.path = path                        # /export/home/bp/cobol/main/src/SAMPLE.cob

    def basename(self):
        return os.path.basename(self.path)      # SAMPLE.cob

    def load(self):
        return self.basename().split('.')[0]    # SAMPLE

    def search_assigned_jcl(self):
        ### 本番機向け
        # 該当プログラムがアサインされているjclを検索し、
        # jclのフルパスをリスト形式で返却する。

        result = []

        # 調査対象jclライブラリ
        jcl_lib = []
        jcl_lib.append("/export/home/bp/jcl")
        jcl_lib.append("/export/home/bp/unyou1/jcl")
        jcl_lib.append("/export/home/bpp/bpw00/*/jcl")

        # 調査対象jclライブラリ配下に存在する全ファイルの全行を検索し、
        # exec文にプログラム名が含まれているか判定する。
        # ※コメント行は除く
        for lib in jcl_lib:
            jcl_list = glob.glob(lib + '/*')
            for jcl in jcl_list:
                try:
                    with open(jcl, "r") as j:
                        for line in j:
                            if line.find("exec " + self.load() + " ") >= 0 and not line[0:2] == "*#":
                                result.append(jcl)
                except Exception as e:
                    print(str(e))

        return result

    def search_using_copy(self):
        ### 開発機向け
        # 該当プログラムが利用しているコピー句を検索し、
        # コピー句名称とプログラム内での該当行をリスト形式で返却する。

        result = []

        # 対象プログラムの全行を検査し、
        # コピー句が指定されている行を判定する。
        # ※コメント行、汎用モジュール用コピー句（BPU2Xxxx）は除く
        with open(self.path, "r") as p:
            for line in p:
                if line.find("COPY ") >= 0 and not line[6] == '*' and line.find("BPU2X") < 0:
                    result.append(line.split()[2].replace('.', ''))
                    # result.append(line.replace('\n', ''))

        return result

        
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    script_name = args[0]

    # 引数チェック
    if num != 2:
        print "Usage: %s program_path_list" % script_name
        quit()

    input_filepath = args[1]

#    with open(input_filepath, "r") as f:
#        cr = csv.reader(f, delimiter="\n")
#
#        for c in cr:
#            for program_path in c:
#                pg = Cobol(program_path)
#                l = []
#                l.append(pg.basename())
#
#                for jcl in pg.search_assigned_jcl():
#                    l.append(jcl)
#
#                with open("/BP/UNY020/s1yst.out", "a") as o:
#                    cw = csv.writer(o)
#                    cw.writerow(l)

    with open(input_filepath, "r") as f:
        cr = csv.reader(f, delimiter="\n")

        for c in cr:
            for pg_path in c:
                cob = CobolAnalyzer(pg_path)
                l = []
                l.append(cob.basename())
                for copy in cob.search_using_copy():
                    l.append(copy)
                with open("/BP/UNY020/" + script_name[:-3] + "_s1yst.out", "a") as o:
                    cw = csv.writer(o, delimiter="\t")
                    cw.writerow(l)

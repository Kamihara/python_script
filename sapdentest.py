#!/usr/bin/python
#! coding: shift-jis

#
# ライブラリインポート
#

import sys
import os

#
# 関数定義
#

def sapdentest(jcl):
    # 定数定義
    wkvol = "/BP/UNY020/"
    jcl_name = os.path.basename(jcl)
    step = []

    with open(wkvol + "test_" + jcl_name, "w") as o:
        with open(jcl, "r") as i:
            while(True):
                # jclを一行ずつ読む
                l = i.readline()
                # 日付マスタ付替え
                if "/BP/FLVP01/YRS.DATE.MST" in l:
                    step.append("*#*" + l)
                    step.append(l.replace("/BP/FLVP01/YRS.DATE.MST", "/BP/FLVP01/SAP.DATE.MST"))
                else:
                    step.append(l)

                # stependまで溜め込み、stependで出力
                if "stepend" in l:
                    # バックアップステップはコメント化
                    for s in step:
                        if "/export/home/bp/sh/BACKUP_DAY.csh" in s:
                            comment_step = []
                            comment_step = map(lambda x: "*#*" + x, step)
                            step = comment_step
                    o.writelines(step)
                    step = []
                # jobendで終了
                if l.startswith("jobend") == True:
                    o.writelines(step)
                    break

#
# メイン処理
#

if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    # 引数チェック
    if num != 2:
        print "Usage: %s jcl" % pgname
        quit()

    jcl = args[1]

    # jclの存在チェック
    if os.path.isfile(jcl) == False:
        print "Error: jcl does not exist"
        quit()

    sapdentest(jcl)

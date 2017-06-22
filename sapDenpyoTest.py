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

def sapDenpyoTestHonban(jcl):
    # 定数定義
    wkvol = "/BP/UNY020/"
    jcl_name = os.path.basename(jcl)
    step = []
    out_jcl = wkvol + jcl_name

    with open(out_jcl, "w") as o:
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
    print(out_jcl + "を作成しました")

def sapDenpyoTestKaihatsu(jcl):
    # 定数定義
    wkvol = "/BP/UNY010/"
    newvol = "/KEIRI1/SAP/BP/"
    jcl_name = os.path.basename(jcl)
    step = []
    out_jcl = wkvol + jcl_name

    with open(out_jcl, "w") as o:
        with open(jcl, "r") as i:
            while(True):
                # jclを一行ずつ読み、パス変換
                l = i.readline().replace("/BP/", newvol)
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
    print(out_jcl + "を作成しました")

#
# メイン処理
#

if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    # 引数チェック
    if num != 3:
        print "Usage: %s jcl type[hon|kai]" % pgname
        quit()

    jcl = args[1]
    type = args[2].lower()

    # jclの存在チェック
    if os.path.isfile(jcl) == False:
        print "Error: jcl does not exist"
        quit()
    
    # 処理区分で分岐
    if type == 'hon':
        sapDenpyoTestHonban(jcl)
    elif type == 'kai':
        sapDenpyoTestKaihatsu(jcl)
    else:
        print "Error: type is not illegal"
        quit()

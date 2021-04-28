#!/usr/bin/python
#! coding: shift-jis

#
# ライブラリインポート
#

import sys
import os
import commands
import csv
import shutil

#
# 関数定義
#

def get_snd_history():

    sndlist = []
    snd_history = commands.getoutput("utllist -s -h WDCB0918").split('\n')
    for l in snd_history:
        sndlist.append(l.split())

    # sndlist[x][0] 'FILEID'
    # sndlist[x][1] 'HOST NAME'
    # sndlist[x][2] 'START DAY'
    # sndlist[x][3] 'START TIME'
    # sndlist[x][4] 'END TIME'
    # sndlist[x][5] 'RECORDS'
    # sndlist[x][6] 'STATUS'
    # sndlist[x][7] 'CONNECT'

    # 過去履歴保存用中間ファイルに追記
    with open("/BP/UNY020/SAP_snd_history.tmp", "a") as tmp:
        writer = csv.writer(tmp, lineterminator='\n')
        for x in range(3, len(sndlist)-1):
            writer.writerow([sndlist[x][0], sndlist[x][2], sndlist[x][3], sndlist[x][4], sndlist[x][5]])

    # 重複排除
    snd_uniqlist = []
    with open("/BP/UNY020/SAP_snd_history.tmp", "r") as tmp:
        reader = csv.reader(tmp)
        for row in reader:
            if row not in snd_uniqlist:
                snd_uniqlist.append(row)
        
    # 重複排除したものをcsvファイルへ
    header = ['FILEID', 'START DAY', 'START TIME', 'END TIME', 'RECORDS']
    with open("/BP/UNY020/SAP_snd_history.csv", "w") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(header)
        for line in snd_uniqlist:
            writer.writerow(line)


def get_rcv_history():

    rcvlist = []
    rcv_history = commands.getoutput("utllist -r -h WDCB0918").split('\n')
    for l in rcv_history:
        rcvlist.append(l.split())

    # rcvlist[x][0] 'HOST NAME'
    # rcvlist[x][1] 'FILEID'
    # rcvlist[x][2] 'START DAY'
    # rcvlist[x][3] 'START TIME'
    # rcvlist[x][4] 'END TIME'
    # rcvlist[x][5] 'RECORDS'
    # rcvlist[x][6] 'STATUS'
    # rcvlist[x][7] 'CONNECT'
    
    # 過去履歴保存用中間ファイルに追記
    with open("/BP/UNY020/SAP_rcv_history.tmp", "a") as tmp:
        writer = csv.writer(tmp, lineterminator='\n')
        for x in range(3, len(rcvlist)-1):
            writer.writerow([rcvlist[x][1], rcvlist[x][2], rcvlist[x][3], rcvlist[x][4], rcvlist[x][5]])

    # 重複排除
    rcv_uniqlist = []
    with open("/BP/UNY020/SAP_rcv_history.tmp", "r") as tmp:
        reader = csv.reader(tmp)
        for row in reader:
            if row not in rcv_uniqlist:
                rcv_uniqlist.append(row)
        
    # 重複排除したものをcsvファイルへ
    header = ['FILEID', 'START DAY', 'START TIME', 'END TIME', 'RECORDS']
    with open("/BP/UNY020/SAP_rcv_history.csv", "w") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(header)
        for line in rcv_uniqlist:
            writer.writerow(line)

#
# メイン処理
#

if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    get_snd_history()
    get_rcv_history()


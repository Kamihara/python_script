#!/usr/bin/python
#coding:utf-8

import sys
import os

def variable_mkdir(root_dir):

    dir_list = "/export/home/s1/s1yst/tool/mkdir_list.txt"
    with open(dir_list, 'r') as list:
        for line in list:
            dir = line.rstrip('\n')
            os.makedirs(root_dir + dir)



if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    # arguments check
    if num != 2:
        print "Usage: %s root_dir" % pgname
        quit()

    root_dir = args[1]

    variable_mkdir(root_dir)

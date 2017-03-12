#!/usr/bin/python
import sys
import os

def lenfix(num, pgname, in_filepath, length):
    # arguments check
    if num != 3:
        print "Usage: %s filepath length" % pgname
        quit()

    # length check
    filesize = os.path.getsize(in_filepath)
    if filesize % length != 0:
        print "Error: length is not collect"
        quit()

    fi = open(in_filepath, 'r')
    content = fi.read()
    fi.close

    out_filepath = "new_" + in_filepath
    fo = open(out_filepath, 'w')

    while content != "":
        #print content[:length]
        fo.write(content[:length] + '\n')
        content = content[length:]

def conv(in_filepath, copyfile):
    # copyfile analyze
    cpy = open(copyfile, 'r')
    for line in cpy:
        cpylist = line.split(' ')
        idx = cpylist.index("PIC")
        if copylist[idx + 1] = "X":
        if copylist[idx + 1] = "9":
        if copylist[idx + 1] = "S9":
        if copylist[idx + 1] = "N":


if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]
    in_filepath = args[1]
    length = int(args[2])

    lenfix(num, pgname, in_filepath, length)

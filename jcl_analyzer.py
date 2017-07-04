#!/usr/bin/python
import sys
import os

def lenfix(num, pgname, in_filepath, length):
    fi = open(in_filepath, 'r')
    content = fi.read()
    fi.close

    out_filepath = in_filepath + "_new"
    fo = open(out_filepath, 'w')

    while content != "":
        fo.write(content[:length] + '\n')
        content = content[length:]



if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    # arguments check
    if num != 3:
        print "Usage: %s filepath length" % pgname
        quit()

    in_filepath = args[1]
    length = int(args[2])

    # file check

    # length check
    filesize = os.path.getsize(in_filepath)
    if filesize % length != 0:
        print "Error: length is not collect"
        quit()

    lenfix(num, pgname, in_filepath, length)

#!/usr/bin/python
import sys
import os
import glob
import csv

def copy_searcher(pgname):
    result = []

    pg_lib = []
    pg_lib.append("/export/home/bp/cobol/main/src")
    pg_lib.append("/export/home/bp/cobol/main/esrc")
    pg_lib.append("/export/home/bp/cobol/sub/src")

    for lib in pg_lib:
        pg_list = glob.glob(lib + '/' + pgname + '.c*')
        for pg in pg_list:
            try:
                with open(pg, "r") as p:
                    for line in p:
                        if line.find("COPY ") >= 0 and not line[6] == '*':
                            copy = line.split()
                            result.append(copy[2].replace('.', ''))
                            result.append(line.replace('\n', ''))
            except Exception as e:
                print(str(e))

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

    with open(in_filepath, "r") as f:
        cr = csv.reader(f, delimiter="\n")
        for c in cr:
            for pgname in c:
                for r in copy_searcher(pgname):
                    l = []
                    l.append(pgname)
                    l.append(r)
                    with open("/BP/UNY020/" + script_name[:-3] + "_s1yst.out", "a") as o:
                        cw = csv.writer(o)
                        cw.writerow(l)

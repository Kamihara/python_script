#!/usr/bin/python
import sys
import os
import glob
import csv

def pg_searcher(pgname):
    result = []
    result.append(pgname)

    jcl_lib = []
    jcl_lib.append("/export/home/bp/jcl")
    jcl_lib.append("/export/home/bpp/bpw00/YHG/jcl")

    for lib in jcl_lib:
        jcl_list = glob.glob(lib + '/*')
        for jcl in jcl_list:
            try:
                with open(jcl, "r") as j:
                    for line in j:
                        if line.find("exec " + pgname) >= 0:
                            result.append(jcl)
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
        cr = csv.reader(f, delimiter=",")
        for c in cr:
            for pgname in c:
                l = []
                for r in pg_searcher(pgname):
                    l.append(r)

                with open("/BP/UNY020/s1yst.out", "a") as o:
                    cw = csv.writer(o)
                    cw.writerow(l)

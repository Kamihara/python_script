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
                        if line.find("COPY ") >= 0 and not line[6] == '*' and line.find("BPU2X") < 0:
                            copy = line.split()
                            result.append(copy[2].replace('.', ''))
                            result.append(line.replace('\n', ''))
            except Exception as e:
                print(str(e))

    return result

def copy_searcher2(copy_list):

    pg_list = []
    for pg in glob.glob('/export/home/bp/cobol/main/src/*'):
        pg_list.append(pg)
    for pg in glob.glob('/export/home/bp/cobol/main/esrc/*'):
        pg_list.append(pg)
    for pg in glob.glob('/export/home/bp/cobol/sub/src/*'):
        pg_list.append(pg)

    copy_lines = []
    for p in pg_list:
        if os.path.basename(p) not in ["PACBREK.cob", "PACEDIT.cob", "PACMAT1.cob", "PACMATN.cob", "PACMATU.cob"]:
            f = open(p, "r")
            lines = f.readlines()
            f.close()
        
        for line in lines:
            if line.find("COPY ") >= 0  and not line[6] == '*' and line.find("BPU2X") < 0:
                copy_lines.append([os.path.basename(p), line])

    result = []
    for copy_line in copy_lines:
        l = copy_line[1].split()
        if l[2] in copy_list:
            result.append([copy_line[0], l[2], copy_line[1]])
            print(result)

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
    copy_list = f.readlines()
    f.close()
    lst = map(lambda x: x.replace("\n", ""), copy_list)
    print(lst)
    
    result = copy_searcher2(lst)
    print(result)
    
    with open("/BP/UNY020/" + script_name[:-3] + "_s1yst.out", "w") as o:
        cw = csv.writer(o, delimiter="\t")
        for l in result:
            row = map(lambda x: x.replace("\n", ""), l)
            cw.writerow(row)

#    with open(in_filepath, "r") as f:
#        cr = csv.reader(f, delimiter="\n")
#        for c in cr:
#            for pgname in c:
#                for r in copy_searcher(pgname):
#                    l = []
#                    l.append(pgname)
#                    l.append(r)
#                    with open("/BP/UNY020/" + script_name[:-3] + "_s1yst.out", "a") as o:
#                        cw = csv.writer(o)
#                        cw.writerow(l)


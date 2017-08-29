#!/usr/bin/python
import sys
import os
import glob
import csv

class CobolProgram(path):
    def __init__(self, path):
        self.basename = os.path.basename(path)
        self.fullpath = path
        self.module = self.basename.split('.')[0]

    def search_assigned_jcl(self):
        result = []

        jcl_lib = []
        jcl_lib.append("/export/home/bp/jcl")
        jcl_lib.append("/export/home/bp/unyou1/jcl")
        jcl_lib.append("/export/home/bpp/bpw00/*/jcl")


        for lib in jcl_lib:
            jcl_list = glob.glob(lib + '/*')
            for jcl in jcl_list:
                try:
                    with open(jcl, "r") as j:
                        for line in j:
                            if line.find("exec " + self.module + " ") >= 0 and not line[0:2] == "*#":
                                result.append(jcl)
                except Exception as e:
                    print(str(e))

        return result

    def search_using_copy(self):
        result = []

        #pg_lib = []
        #pg_lib.append("/export/home/bp/cobol/main/src")
        #pg_lib.append("/export/home/bp/cobol/main/esrc")
        #pg_lib.append("/export/home/bp/cobol/sub/src")

        with open(self.fullpath, "r") as p:
            for line in p:
                if line.find("COPY ") >= 0 and not line[6] == '*' and line.find("BPU2X") < 0:
                    result.append(line.split()[2].replace('.', ''))
                    result.append(line.replace('\n', ''))

        return result

        
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    script_name = args[0]

    # arguments check
    if num != 2:
        print "Usage: %s program_path_list" % script_name
        quit()

    input_filepath = args[1]

    with open(input_filepath, "r") as f:
        cr = csv.reader(f, delimiter="\n")

        for c in cr:
            for program_path in c:
                pg = CobolProgram(program_path)
                l = []
                l.append(pg.basename)

                for jcl in pg.search_assigned_jcl:
                    l.append(jcl)

                with open("/BP/UNY020/s1yst.out", "a") as o:
                    cw = csv.writer(o)
                    cw.writerow(l)

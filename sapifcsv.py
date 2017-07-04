#!/usr/bin/python
import sys
import os


def sapifcsv(filepath, filetype):
    if filetype = "denpyo":
        layout = {
                  { colname: "aaa", collength: 472 }
                 }
        record_length = 472
    if filetype = "tokui":
        layout = {
                  { colname: "aaa", collength: 472 }
                 }
        record_length = 472
    if filetype = "siire":
        layout = {
                  { colname: "aaa", collength: 472 }
                 }
        record_length = 472

    with open(filepath, 'r') as infile:
        content = infile.read()

    out_filepath = in_filepath + ".csv"

    with open(out_filepath, 'w') as outfile:
        for colname in layout:
            fo.write(colname + ",")
        while content != "":
            # for SAPIF
            if content[:2] in ["HH", "TT"]:
                continue
            else:
                fo.write(content[:collength] + ",")
            content = content[record_length:]


#
# main
#

if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    # arguments count check
    if num != 3:
        print "Usage: %s filepath length" % pgname
        quit()

    filepath = args[1]
    filetype = args[2].lower()

    # file check
    if os.path.isfile(filepath) == False:
        print "Error: input file does not exist"
        quit()

    # length check
    filesize = os.path.getsize(in_filepath)
    if filesize % length != 0:
        print "Error: length is not collect"
        quit()

    sapifcsv(filepath, filetype)

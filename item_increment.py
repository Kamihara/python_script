#!/usr/bin/python
import sys
import os

args = sys.argv
argnum = len(args)
pgname = args[0]

#
# error check
#

# arguments check
if argnum != 5:
#    print "Usage: %s in_filepath data_length new_value item_position" % pgname
    print "Usage: %s in_filepath data_length item_position item_length" % pgname
    quit()

in_filepath = args[1]
data_length = int(args[2])
item_position = int(args[3])
item_length = int(args[4])

# file check
if os.path.isfile(in_filepath) == False:
    print "Error: input file does not exist"
    quit()

# data_length check
filesize = os.path.getsize(in_filepath)
if filesize % data_length != 0:
    print "Error: data_length is illegal"
    quit()

#
# main
#

fi = open(in_filepath, 'r')
content = fi.read()
fi.close

filename = in_filepath.split('/')[-1]
#out_filepath = "/BP/UNY020/SAPtest/" + filename + "_new"
#out_filepath = "/BP/UNY020/SAPtest2/" + filename + "_new"
out_filepath = "/BP/UNY020/SAPtest3/" + filename + "_new"
fo = open(out_filepath, 'w')
max_rec_count = filesize / data_length
rec_count = 0

while rec_count < max_rec_count:
    # for SAPIF
    start = rec_count * data_length
    if content[start : start + 2] in ["HH", "TT"]:
        fo.write(content[start : start + data_length])
    else:
        new_value = str(int(content[start + item_position : start + item_position + item_length]) + 1).zfill(item_length)
        fo.write(content[start : start + item_position] + new_value + content[start + item_position + item_length : start + data_length])
    rec_count += 1

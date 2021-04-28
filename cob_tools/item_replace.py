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
    print "Usage: %s in_filepath length new_value item_position" % pgname
    quit()

in_filepath = args[1]
length = int(args[2])
new_value = args[3]
item_position = int(args[4])

# file check
if os.path.isfile(in_filepath) == False:
    print "Error: input file does not exist"
    quit()

# length check
filesize = os.path.getsize(in_filepath)
if filesize % length != 0:
    print "Error: length is illegal"
    quit()

#
# main
#

fi = open(in_filepath, 'r')
content = fi.read()
fi.close

out_filepath = in_filepath + "_new"
fo = open(out_filepath, 'w')

while content != "":
    # for SAPIF
    if content[:2] in ["HH", "TT"]:
        fo.write(content[:length])
    else:
        fo.write(content[:item_position] + new_value + content[item_position + len(new_value):length])
    content = content[length:]

#!/usr/bin/python3

# regular expression is very powerful method to find out any matching word and more

import re

# files = open('file.txt')
#
# for readLines in files:
#     length = len(readLines)
#     # print(len(readLines)) # highest is 24
#     print(readLines[0:23]) # upto this it will produce every sequence
# files.close()
# print("############")
# files = open('file.txt')
# for readLines in files:
#     length = len(readLines)
#     print(readLines[0:-1]) # it will produce every sequence
# files.close()

files = open('file.txt')
for line in files:
    if re.search('(ni|li|pi|di)ne', line):
        print(line, end=' ')

files.close()

print("\n######################")

files = open('file.txt')
for line in files:
    match = re.search('(ni|li|pi|di)ne', line)
    # regular expression is case sensitive. it searches from the start and once gets the match it stops.
    if match:
        print(match.group())

files.close()
############
# first line lenore
#  it is nine, second line and dine
#  third line and never-moreover
#  fifth pine line
# ######################
# line
# nine
# line
# pine
############
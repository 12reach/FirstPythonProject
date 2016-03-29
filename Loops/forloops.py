#!/usr/bin/python3

songs = open('file.txt')

for lines in songs.read():
    print(lines, end='')

# enumerate

songs = open('file.txt')

for index, lines in enumerate(songs.readlines()):
    print(index, lines, end='')

strings = "This is a string."

# now we are going to find how many 's' is inside this string
for index, s in enumerate(strings):
    if s == 's':
        print("Hi I am 's' and I am located at position {}".format(index))


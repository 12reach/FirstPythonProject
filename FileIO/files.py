#!/usr/bin/python3

# infile = open('files.txt', 'r')
#
# outfile = open('new.txt', 'w')

# for line in infile:
#     print(line, file=outfile)
# print("Done")

# let us set the buffersize first

BufferSize = 500000

infile = open('files.txt', 'r')

outfile = open('new.txt', 'w')

buffer = infile.read(BufferSize)

while len(buffer):
    outfile.write(buffer)
    print("It is copying, it might take some time...please wait....", end='')
    buffer = infile.read(BufferSize)

print()
print("Copying Done.")






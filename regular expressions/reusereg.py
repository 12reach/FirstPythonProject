#!/usr/bin/python3

import re

def main():
    CompilerAndReplaceWord()


def CompilerAndReplaceWord():
    try:
        files = open("../primary/file.txt")
        # you can search any pattern that can match ignoring the upper or lower case
        pattern = re.compile('(len|neverm)ore', re.IGNORECASE)
        for line in files:
            # re module search that pattern in a line
            if re.search(pattern, line):
                # we found that patetrn and now it is time to replace them with a new string
                print(pattern.sub("######", line), end=' ')


    except FileNotFoundError as e:
        print("File was not found:", e)

if __name__ == "__main__":
    main()
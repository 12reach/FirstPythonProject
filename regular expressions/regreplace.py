#!/usr/bin/python3
import re

def main():
    ReplaceWord()
    DEmarcationLine()
    MatchAndReplaceWord()



def ReplaceWord():
    try:
        files = open("../primary/file.txt")
        for line in files:
            # you can search any word
            print(re.sub('lenor|more', "#####", line), end=' ')
    except FileNotFoundError as e:
        print("File was not found:", e)

def MatchAndReplaceWord():
    try:
        files = open("../primary/file.txt")
        for line in files:
            # you can search any pattern that can match and then replace with this word
            match = re.search('(len|neverm)ore', line)
            if match:
                print(line.replace(match.group(), "#####"), end=' ')

    except FileNotFoundError as e:
        print("File was not found:", e)

def DEmarcationLine():
    print("*************")


if __name__ == "__main__":
    main()
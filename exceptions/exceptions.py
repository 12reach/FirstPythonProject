#!/usr/bin/python3

def main():
    FileRead()
    DemarcationLine()
    LineStrip()
    DemarcationLine()
    CheckFileExtension()

def ReadFile(filename):
    files = open(filename)
    lines = files.readlines()
    for index, line in enumerate(lines):
        print(index, "=", line)

def StripFile(filename):
    files = open(filename)
    for lines in files:print(lines.strip())


def RaisingError(filename):
    if filename.endswith(".txt"):
        lines = open(filename)
        for line in lines:print(line.strip())
    else:
        raise ValueError("File must end with .txt")

def FileRead():
    try:
        ReadFile("../primary/files.txt") # path is okay, it reads file
    except IOError as e:
        print("Could not open file:", e)

def LineStrip():
    try:
        StripFile("primary/files.txt")
    except IOError as e:
        print("Could not open file:", e) # it will give error


def CheckFileExtension():
    try:
        RaisingError("../primary/file.rtf")
    except IOError as e:
        print("Could not open file:", e)
    except ValueError as e:
        print("Bad Filename:", e)


def DemarcationLine():
    print("******************")

if __name__ == "__main__":
    main()
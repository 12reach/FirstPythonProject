#!/usr/bin/python3

def main():

    strings = "I love you."
    print(strings)

    anotherStrings = "I love you but\nI don't know how much you love me."
    print(anotherStrings)

    rawStrings = r"I love you but\nI don't know how much you love me."
    print(rawStrings)

    days = 8
    lyrics = "%s days a week is not enough to love you." %days
    print(lyrics)

    days = 8
    lyrics = "{} days a week is not enough to love you."
    print(lyrics.format(days))

    newLines = """\
    first line
    second line
    thiord line
    more to come...
    """
    print(newLines)

if __name__ == "__main__":
    main()


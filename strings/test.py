#!/usr/bin/python3

# s = 'this is a string'
#
# print(s.find('is'))
#
# newstring = s.replace('this', 'that')
#
# print(newstring)
#
# UpperString = s.upper()
#
# print(UpperString)
#
# # string is mutable, so id has been changed for the same string
# print(id(s))
# print(id(UpperString))
#
# a = '    this is string with lot of whitespace at the beginning and at the end     '
# # by default it removes white space from start and end
# RemovingWhiteSpace = a.strip()
# print(RemovingWhiteSpace)
# print(RemovingWhiteSpace.strip('this'))
#
# x, y = 10, 11
#
# f = "this {} is added and thereafter we add {}"
# FormattedString = f.format(x, y)
#
# print(FormattedString)
#
# # we could have written it in C style
# m, n = 10, 11
#
# f = "this %d is added and thereafter we add %d"
# FormattedString = f % (x, y)
#
# print(FormattedString)


# a, b = 10, 11
#
# s = "This is {}, and that is {}"
#
# FormattedStirng = s.format(a, b)
#
# print(FormattedStirng)
#
# # we change the position
#
# FormattedStirng = s.format(b, a)
#
# print(FormattedStirng)
#
# s = "This is {0}, and that is {1} and this too is {0} and that too is {1}"
#
# FormattedStirng = s.format(a, b)
#
# print(FormattedStirng)
#
# # we can change it according to our wish with the positional argument
#
# s = "This is {1}, and that is {1} and this too is {0} and that too is {1}"
#
# FormattedStirng = s.format(a, b)
#
# print(FormattedStirng)
#
# # we can use it as dictionary
#
# s = "This is {mine}, and that is {your} and this too is {your} and that too is {mine}"
#
# FormattedStirng = s.format(mine = a, your = b)
#
# print(FormattedStirng)
#
# # more dictionary staff
#
# s = "This is my wish: {mine}, and that is your wish :{your} and this too is mine: {mine} and that too is mine: {mine}"
#
# FormattedStirng = s.format(mine = "I want to remove 'I'", your = "Do you want to remove 'yourself'?")
#
# print(FormattedStirng)

strings = "This is a string"

print(type(strings))
print(id(strings))

AnotherStrings = "This is a string"

print(type(AnotherStrings))
print(id(AnotherStrings))


print(strings.split())

words = strings.split()
words.append("and that ia also a string.")

print(type(words))

print(words[0])
NewWords = ":".join(words)
print(NewWords)
NewWords = ",".join(words)
print(NewWords)

words[0] = "That"
print(words)
#!/usr/bin/python3

a = 1
b = "b"
c = (1,2,4,8)
d = ['mana', 'babu', 'hagudu']
e = {'name':'mana', 'age':7, 'look':'sweet'}

def main():
    print(type(a), a)
    print(type(b),b)
    print(type(c),c)
    print(type(d),d)
    print(type(e),e)

if __name__ == "__main__":main()

# in python everything is oject and has an associated class along with it
# we can have an output like this

# <class 'int'> 1
# <class 'str'> b
# <class 'tuple'> (1, 2, 4, 8)
# <class 'list'> ['mana', 'babu', 'hagudu']
# <class 'dict'> {'look': 'sweet', 'name': 'mana', 'age': 7}
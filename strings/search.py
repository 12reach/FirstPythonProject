#!/usr/bin/python3

users = {'name' : ['mana', 'babu', 'bappa'], 'pasword' : ['mm', 'bb', 'bb']}

# print(users['name'][0])

# print(users['name'])
# print(len(users['name']))

totalNumberOfUsers = len(users['name'])
print(totalNumberOfUsers)

def searchingNames(name):
    for i in range(0, totalNumberOfUsers):
        if users['name'][i] == name:
            print("Found!")
            break
        else:
            continue
    print("If you already see above 'Found', the user is in the list. If you don't, the user is not in the list.")

searchingNames('bappa')

def searchNames(name):
    if name in users.get('name', name):
        print("Found")
    else:
        print("Not found.")

searchNames('mana') # Found
searchNames('man') # Not found


# there are two functions which do the same action - searching a table; but the second one is close to perfection.


# we can take input from a user and search through a large text file and try to find if any word is there.


# hint and dictionary

previousValue = {0:1, 1:1}
print(previousValue.get(0))

def fibonachi(n):
    if previousValue.get(n, 0):
        return previousValue[n]
    else:
        newValue = fibonachi(n-1) + fibonachi(n-2)
        previousValue[n] = newValue
        return newValue

print(fibonachi(40)) # 165580141

myValue = fibonachi(10)

myFile = open('strings.txt', 'w')

myFile.write(str(myValue))

myFile.close()









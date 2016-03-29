#!usr/bin/python3

EnglishDictionaries = {'bare':'jejune', 'anger':'dudgeon', 'abuse':'vituperate', 'howl':'ululate'}
print(EnglishDictionaries)

# getting in a nmore human readable form
for keys in EnglishDictionaries:
    print(keys, "=", EnglishDictionaries[keys])

print("***************")

EnglishDictionaries = {'bare':'jejune', 'anger':'dudgeon', 'abuse':'vituperate', 'howl':'ululate'}
for keys in sorted(EnglishDictionaries.keys()):
    print(keys, "=", EnglishDictionaries[keys])

print("***************")

EnglishDictionaries = dict(
    bare='jejune', anger='dudgeon', abuse= 'vituperate', howl= 'ululate', eatable= 'comestible'
)
for keys in sorted(EnglishDictionaries.keys()):
    print(keys, "=", EnglishDictionaries[keys])
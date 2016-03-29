#!usr/bin/python3

import unittest

import modules.modules, Databases.MySQLite1

class TestVersionOfPython(unittest.TestCase):
    def __init__(self):
        modules.modules.PyVer()
    def DisplaySQLiteDB(self):

        Databases.MySQLite1.main()

test = TestVersionOfPython()
# print(test.DisplaySQLiteDB())
test.DisplaySQLiteDB()

if __name__ == "__main__":
    unittest.main()
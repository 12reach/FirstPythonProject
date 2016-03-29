#!/usr/bin/python3

from mysql.connector import MySQLConnection, Error

from MySQL_Connector.mysql_config import ReadingMySQLConfig

def Connect():

    kwargs = ReadingMySQLConfig()
    MyConnection = MySQLConnection(**kwargs)
    try:
        if MyConnection.is_connected():
            print("Connected")
    except Error as e:
        print(e)
    finally:
        MyConnection.close()

if __name__ == "__main__":
    Connect()






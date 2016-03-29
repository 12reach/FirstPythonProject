#!/usr/bin/python3

from mysql.connector import MySQLConnection, Error

from MySQL_Connector.mysql_config import ReadingMySQLConfig

def InsertBooks(books):
    query = "INSERT INTO books(title, isbn) VALUES(%s, %s)"
    try:
        kwargs = ReadingMySQLConfig()
        MyConnection = MySQLConnection(**kwargs)
        if MyConnection.is_connected():
            cursor = MyConnection.cursor()
            cursor.executemany(query, books)
            MyConnection.commit()
    except Error as e:
        print(e)
    finally:
        MyConnection.close()

def main():
    # books = [("Gitanjali", 123456), ("Words", 765432), ("Farewell to Arms", 12457896)]
    books = [("TestBook", 1236547890)]
    InsertBooks(books)
    print("Inserted one book")

if __name__ == "__main__":
    main()
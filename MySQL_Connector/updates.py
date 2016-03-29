#!/usr/bin/python3

from mysql.connector import MySQLConnection, Error

from MySQL_Connector.mysql_config import ReadingMySQLConfig

def UpdateBooks(book_id, title):
    kwargs = ReadingMySQLConfig()
    data = (title, book_id)
    query = "UPDATE books SET title = %s WHERE id = %s"
    try:
        MyConnection = MySQLConnection(**kwargs)
        cursor = MyConnection.cursor()
        cursor.execute(query, data)
        MyConnection.commit()
    except Error as e:
        print(e)
    finally:
        MyConnection.close()

def main():
    for id in range(1, 25):
        if id == 3:
            UpdateBooks(id, "I Have A Dream")
            print("One book has been updated")
        elif id == 4:
            UpdateBooks(id, "Laravel 5 Unfolded")
            print("One book has been updated")
        elif id == 5:
            UpdateBooks(id, "Play With Python")
            print("One book has been updated")


if __name__ == "__main__":
    main()
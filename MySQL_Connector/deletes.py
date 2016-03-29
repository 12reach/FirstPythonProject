#!/usr/bin/python3

from mysql.connector import MySQLConnection, Error

from MySQL_Connector.mysql_config import ReadingMySQLConfig

def DeleteBooks(book_id):
    kwargs = ReadingMySQLConfig()
    query = "DELETE FROM books WHERE id = %s"
    try:
        MyConnection = MySQLConnection(**kwargs)
        cursor = MyConnection.cursor()
        cursor.execute(query, (book_id,))
        # why , is given?
        MyConnection.commit()
    except Error as e:
        print(e)
    finally:
        MyConnection.close()

def main():
    id = 87
    DeleteBooks(id)
    print("Deleted ", id, "number of book from books")


if __name__ == "__main__":
    main()
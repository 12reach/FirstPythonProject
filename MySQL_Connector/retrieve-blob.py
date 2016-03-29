#!/usr/bin/python3

from mysql.connector import MySQLConnection, Error

from MySQL_Connector.mysql_config import ReadingMySQLConfig


def WriteFile(data, filename):
    with open(filename, 'wb') as files:
        files.write(data)

def ReadImage(author_id, filename):
    kwargs = ReadingMySQLConfig()
    query = 'SELECT photo FROM authors WHERE id = %s'
    try:
        MyConnection = MySQLConnection(**kwargs)
        cursor = MyConnection.cursor()
        cursor.execute(query, (author_id,))
        photo = cursor.fetchone()[0]
        WriteFile(photo, filename)
    except Error as e:
        print(e)
    finally:
        MyConnection.close()

def main():
    id = 47
    ReadImage(id, "/home/hagudu/Pictures/ss1.jpg")



if __name__ == "__main__":
    main()
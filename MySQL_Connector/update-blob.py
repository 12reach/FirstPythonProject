#!/usr/bin/python3

from mysql.connector import MySQLConnection, Error

from MySQL_Connector.mysql_config import ReadingMySQLConfig

def ReadFile(filename):
    with open(filename, 'rb') as f:
        images = f.read()
    return images

def UpdateImage(author_id, filename):
    kwargs = ReadingMySQLConfig()
    data = ReadFile(filename)
    query = "UPDATE authors SET photo = %s WHERE id = %s"
    args = (data, author_id)
    try:
        MyConnection = MySQLConnection(**kwargs)
        cursor = MyConnection.cursor()
        cursor.execute(query, args)
        MyConnection.commit()
    except Error as e:
        print(e)
    finally:
        MyConnection.close()

def main():
    id = 47
    UpdateImage(id, "/home/hagudu/Pictures/ss.jpg")
    print("Image of author ID", id, "has been updated.")


if __name__ == "__main__":
    main()
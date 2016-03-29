#!/usr/bin/python3

from mysql.connector import MySQLConnection, Error
from Databases.python_mysql_dbconfig import read_db_config


def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM EMPLOYEE")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print("First Name = ", row[0])
            print("Second Name = ", row[1])
            print("Age = ", row[2])
            print("Sex = ", row[3])
            print("Salary = ", row[4])

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchall()
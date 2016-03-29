#!/usr/bin/python3

import mysql.connector

from mysql.connector import Error


def ConnectionTest():
### connecting to MySQL Database ###
    try:
        ### you can either use a dictionary object or you can connect directly ###
        ### using a dictioanry object ###
        kwargs = dict(host = 'localhost', database = 'python_mysql', user = 'root', password = 'pass')
        conn = mysql.connector.connect(**kwargs)
        ### connecting directly ###
        connection = mysql.connector.connect(host = 'localhost',
                                             database = 'python_mysql',
                                             user = 'root',
                                             password = 'pass')
        if conn.is_connected():
            print("Connected from 'conn' object")

    except Error as e:
        print(e)

    finally:
        connection.close()


if __name__ == "__main__":
    ConnectionTest()




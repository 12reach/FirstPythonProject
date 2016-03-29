#!/usr/bin/python3

import mysql.connector

from mysql.connector import Error

def RetievwValues():

    try:
        kwargs = dict(host = 'localhost', database = 'python_mysql', user = 'root', password = 'pass')
        conn = mysql.connector.connect(**kwargs)

    ### shows you how to query data from a MySQL database in Python by using MySQL Connector/Python API
    # such as fetchone() , fetchmany() , and fetchall() ###
        if conn.is_connected():
            cursors = conn.cursor()
            cursors.execute('SELECT * FROM authors')
            # row = cursors.fetchone()
            # output (1, 'Bel and the Dragon ', '123828863494')
            ######
            # now we try to get all the books
            # row = cursors.fetchall()
            # print(type(row))
            # output <class 'list'>, so we can use for loop
            # for books in row:
            #     print(books)
            # it will give us list of all the books
            ######

            ### now we give the size of how many books we want to get ###
            # HowManyBooks = 8
            # row = cursors.fetchmany(HowManyBooks)
            # for books in row:
            #     print(books)
            # we get the output of 8 books

            row = cursors.fetchall()

            for books in row:
                print(books)


    except Error as e:
        print(e)

    finally: conn.close()


if __name__ == "__main__":
    RetievwValues()
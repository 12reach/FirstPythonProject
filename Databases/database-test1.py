#!/usr/bin/python3


import sqlite3

def main():

    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row

    db.execute('drop table if exists test1')

    db.execute('create table test1 (t1 text, i1 int)')

    db.execute('insert into test1 (t1, i1) values (?, ?)', ('Babu', 1))
    db.execute('insert into test1 (t1, i1) values (?, ?)', ('Mana', 2))
    db.execute('insert into test1 (t1, i1) values (?, ?)', ('Bappa', 3))
    db.execute('insert into test1 (t1, i1) values (?, ?)', ('Babua', 4))
    db.execute('insert into test1 (t1, i1) values (?, ?)', ('Anju', 5))
    db.execute('insert into test1 (t1, i1) values (?, ?)', ('Patai', 6))
    db.execute('insert into test1 (t1, i1) values (?, ?)', ('GasaBuddhu', 7))
    db.execute('insert into test1 (t1, i1) values (?, ?)', ('Tapas', 8))
    db.commit()

    DatabaseRead = db.execute('select * from test order by i1')
    for row in DatabaseRead:
        # print(dict(row))
        print(row['t1'])
        # print(row['t1'], row['i1'])
    # print(type(row))

if __name__ == "__main__":main()
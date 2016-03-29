#!/usr/bin/python3


import sqlite3

def create(db, row):
    db.execute('insert into MyFirstSQLiteTable (username, id) values (?, ?)', (row['username'], row['id']))
    db.commit()

def retrieve(db, username):
    cursor = db.execute('select * from MyFirstSQLiteTable where username = ?', (username,))
    return cursor.fetchone()

def update(db, row):
    db.execute('update MyFirstSQLiteTable set id = ? where username = ?', (row['id'], row['username']))
    db.commit()

def delete(db, username):
    db.execute('delete from MyFirstSQLiteTable where username = ?', (username,))
    db.commit()

def DisplayRows(db):
    cursor = db.execute('select * from MyFirstSQLiteTable order by username')
    for row in cursor:
        print('  {}: {}'.format(row['username'], row['id']))

def main():
    db = sqlite3.connect('MyFirstSQLiteDB.db')
    db.row_factory = sqlite3.Row
    print('Create table MyFirstSQLiteTable')
    db.execute('drop table if exists MyFirstSQLiteTable')
    db.execute('create table MyFirstSQLiteTable ( username text, id int )')

    print('Create rows')
    create(db, dict(username = 'babu', id = 1))
    create(db, dict(username = 'mana', id = 2))
    create(db, dict(username = 'pata', id = 3))
    create(db, dict(username = 'gopal', id = 4))
    create(db, dict(username = 'bappa', id = 5))
    create(db, dict(username = 'babua', id = 6))
    create(db, dict(username = 'buddhu', id = 7))
    DisplayRows(db)

    print('Retrieve rows')
    print(dict(retrieve(db, 'babu')), dict(retrieve(db, 'mana')))

    print('Update rows')
    update(db, dict(username = 'Tapas', id = 7))
    # update(db, dict(username = 'three', id = 103))
    DisplayRows(db)

    # print('Delete rows')
    # delete(db, 'one')
    # delete(db, 'three')
    # DisplayRows(db)

if __name__ == "__main__":
    main()
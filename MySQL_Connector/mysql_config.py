#!/usr/bin/python3

from configparser import ConfigParser

# parser = ConfigParser()
#
# parser.read(filenames= 'mysql_config.ini')
# db = dict()
# if parser.has_section(section= 'mysql'):
#     items = parser.items(section= 'mysql')
#     for item in items:
#         # converting tuplea into dictionary
#         db[item[0]] = item[1]
# print(db)

def ReadingMySQLConfig(filemame = 'mysql_config.ini', section = 'mysql'):

    parser = ConfigParser()
    parser.read(filemame)
    db = dict()
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
            raise Exception('{0} not found in the {1} file'.format(section, filemame))

    return db



#!/usr/bin/python3
"""
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb as mysql
from sys import argv

if __name__ == '__main__':

    try:
        db = mysql.connect(
            host='localhost',
            port=3306,
            passwd=argv[1],
            user=argv[2],
            db=argv[3]
        )

    except Exception:
        print("failed to connect to database")
        exit(0)

    name = argv[4]
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE \
                    name = BINARY '{:s}';".format(name))
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()

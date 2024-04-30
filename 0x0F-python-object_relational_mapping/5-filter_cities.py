#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb as mysql
from sys import argv

if __name__ == "__main__":
    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print("database connection failed")
        exit(0)

    searched = argv[4]
    cur = db.cursor()
    cur.execute("""SELECT c.name \
                FROM cities as c \
                INNER JOIN states as s \
                ON c.state_id = s.id \
                WHERE s.name = '{:s}' \
                ORDER BY c.id ASC;""".format(searched))

    res = cur.fetchall()

    final = []
    for i in range(len(res)):
        final.append(res[i][0])

    print(', '.join(final))

    cur.close()
    db.close()

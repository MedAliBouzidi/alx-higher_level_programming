#!/usr/bin/python3
"""
    takes in the name of a state as an argument
    and lists all cities of that state, using
    the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print('<Usage>: ./5-filter_cities.py\
            [mysql_username] [mysql_password] [database name]\
            [state name]')
    else:
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT c.id, c.name\
                    FROM cities AS c INNER JOIN states AS s\
                    ON s.id=c.state_id and s.name=%s ORDER BY id", (sys.argv[4], ))
        rows = cur.fetchall()
        res = []
        for row in rows:
            res.append(row[1])
        print(', '.join(res))
        cur.close()
        conn.close()

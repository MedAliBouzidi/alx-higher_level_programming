#!/usr/bin/python3
"""
    takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where
    name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print('<Usage>: ./3-my_safe_filter_states.py\
            [mysql_username] [mysql_password] [database name]\
             [state name]')
    else:
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE name \
            LIKE %s ORDER BY id", (sys.argv[4], ))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()

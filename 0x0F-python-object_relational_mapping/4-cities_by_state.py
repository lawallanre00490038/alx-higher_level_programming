#!/usr/bin/python3
"""Write a script that takes in an argument the states of hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("select cities.id, cities.name, states.name\
                from cities\
                inner join states\
                on states.id = cities.id\
                order by cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

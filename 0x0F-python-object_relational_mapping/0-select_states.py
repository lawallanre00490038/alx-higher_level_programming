#!/usr/bin/python3

"""
Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

if __name__ == "__main__":
  import MySQLdb
  import sys

  db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
  cur = db.cursor()
  rows = cur.execute("SELECT * FROM states ORDER BY states.id;")
  rows = cur.fetchall()
  
  for row in rows:
    print((row[0], row[1]))

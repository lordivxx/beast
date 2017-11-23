#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_all_character(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM character")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def main():
    database = "beast.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        select_all_character(conn)
 
 
if __name__ == '__main__':
    main()

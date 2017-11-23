#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error
 
 
def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(':memory:')
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_character(conn, character):
    sql = ''' INSERT INTO character(name,hp,atk,def,disc)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, character)
    return cur.lastrowid

def create_mob(conn, mob):
    sql = ''' INSERT INTO mob(name,hp,atk,def,disc)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, mob)
    return cur.lastrowid

 
 
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
 
 
def select_character_stat(conn,stat):
    sql = "SELECT %s FROM character" % stat
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_mob_stat(conn,stat):
    sql = "SELECT %s FROM mob" % stat
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def create_database(conn):
    sql_create_character_table = """ CREATE TABLE IF NOT EXISTS character (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        hp interger NOT NULL,
                                        atk interger NOT NULL,
                                        def interger NOT NULL,
                                        disc text
                                    ); """

    sql_create_mob_table = """CREATE TABLE IF NOT EXISTS mob (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        hp interger NOT NULL,
                                        atk interger NOT NULL,
                                        def interger NOT NULL,
                                        disc text
                                );"""

    if conn is not None:
        # create character table
        create_table(conn, sql_create_character_table)
        create_table(conn, sql_create_mob_table)
        # create mob table
        #create_table(conn, sql_create_mob_table)
        characterdetails = ('IVXX', 100, 2, 1, '1st character');
        mobdetails = ('Owl', 200, 2, 1, '1st mob');
        character_id = create_character(conn, characterdetails)
        mob_id = create_mob(conn, mobdetails)
    else:
        print("Error! cannot create the database connection.")

 
 
def main():

    conn = create_connection()
    with conn:
        create_database(conn)
        #select_all_character(conn)
        select_character_stat(conn,'name')
        select_mob_stat(conn,'name')
 
 
if __name__ == '__main__':
    main()

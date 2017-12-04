#! /usr/bin/python


# Beast game by Charles Forsyth 2017

####### Load modules ##########
import subprocess
from subprocess import Popen, PIPE
import time
import os
import sys
import random
import argparse
import ConfigParser
from IVXX import IVXX
import signal
import sqlite3
from sqlite3 import Error


###### setting argument requierments with ArgParse 
parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-c", "--charactercfg" , help='The path to a character config file', required=False)
requiredNamed.add_argument("-m", "--mobcfg" , help='The path to a mob config file', required=False)
requiredNamed.add_argument("-d", "--dbinit" , help='Init the db', required=False)
requiredNamed.add_argument("-i", "--interactive" , help='interactive', required=False)
requiredNamed.add_argument("-f", "--fight_function" , help='fight_function', required=False)
args = parser.parse_args()


######## Assign Variables  ######
charactercfg = args.charactercfg
mobcfg = args.mobcfg


######## Assign Variables  ######
charactercfg = args.charactercfg
if charactercfg == None:
    charactercfg = "/rhome/forsythc/.character.cfg"
mobcfg = args.mobcfg
if mobcfg == None:
    mobcfg = "/rhome/forsythc/.mob.cfg"

dbinit = args.dbinit
interactive = args.interactive
fight_function = args.fight_function
if fight_function == None:
    fight_unction = 'n'
######## Functions #########


def signal_handler(signal, frame):
    #print('Beast is closed!')
    sys.exit(0)

def create_character(conn,character):
    sql = ''' INSERT INTO character(name,hp,atk,def,disc)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, character)
    return cur.lastrowid

def create_mob(conn,mob):
    sql = ''' INSERT INTO mob(name,hp,atk,def,disc)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, mob)
    return cur.lastrowid



def select_all_rooms(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM adv1_map")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_all_character(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM character")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_all_mob(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mob")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def update_charcter_stat(conn,stat,statupdate):
    sql = "UPDATE character SET %s = %s " % (stat,statupdate)
    cur = conn.cursor()
    cur.execute(sql)

def visit_healer(conn,statupdate):
    update_charcter_stat(conn,'hp',statupdate)

def select_character_stat(conn,stat):
    sql = "SELECT %s FROM character" % stat
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        #print(row[0])
        return row[0]

def create_connection():
    try:
        dbfile = "/rhome/forsythc/repos/beast/beast.db"
        conn = sqlite3.connect(dbfile)
        #conn = sqlite3.connect(':memory:')
        return conn
    except Error as e:
        print(e)

    return None

def commit_db(conn):
    conn.commit()

def close_db(conn):
    conn.close()

def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def select_mob_stat(conn,stat):
    sql = "SELECT %s FROM mob" % stat
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        #print(row[0])
        return row[0]

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

    sql_create_adventure_map_table = """CREATE TABLE IF NOT EXISTS adv1_map (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        geoidy interger NOT NULL,
                                        geoidx interger NOT NULL,
                                        disc text NOT NULL,
                                        mobden interger NOT NULL
                                        );"""

    if conn is not None:
        # create character table
        #create_table(conn, sql_create_character_table)
        #create_table(conn, sql_create_mob_table)
        create_table(conn, sql_create_adventure_map_table)
        # create mob table
        #characterdetails = (beast_name, beast_hp, beast_atk, beast_def, '1st character');
        #mobdetails = (mob_name, mob_hp, mob_atk, mob_def, '1st mob');
        #character_id = create_character(conn, characterdetails)
        #mob_id = create_mob(conn, mobdetails)
        commit_db(conn)
    else:
        print("Error! cannot create the database connection.")

def add_rooms(conn):
    mobs = [('North Room', 0, 1, 'This is the North Room', 35),
            ('South Room', 0, -1, 'This is the South Room', 1),
            ('East Room', 1, 0, 'This is the East Room', 1),
            ('West Room', -1, 0, 'This is the West Room', 15)],
            ('Northeast Room', 1, 1, 'This is the Northeast Room', 35),
            ('Southeast Room', 1, -1, 'This is the Southeast Room', 1),
            ('Northwest Room', -1, 1, 'This is the Northwest Room', 1),
            ('Southwest Room', -1, -1, 'This is the Southwest Room', 15),
            ('BaseCamp', 0, 0, 'This is the BaseCamp', 15)]
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO adv1_map(name, geoidy, geoidx, disc, mobden) VALUES(?,?,?,?,?)''', mobs)
    conn.commit()

def add_mobs(conn):
    mobs = [('Rator', 50, 2, 1),
            ('Tauren', 100, 2, 1),
            ('Cat', 75, 15, 1),
            ('Dragon', 200, 2, 15)]
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO mob(name, hp, atk, def) VALUES(?,?,?,?)''', mobs)
    conn.commit()

def del_all_mobs(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mob")
    conn.commit()

    


########## Main Code ##########
if __name__ == '__main__':

    # Load the class
    #x = IVXX(os.environ['USER'],fight_function)
    signal.signal(signal.SIGINT, signal_handler)
    conn = create_connection()
    #create_database(conn)
    add_rooms(conn)
    #select_all_character(conn)
    select_all_rooms(conn)
    #select_all_mob(conn)
    #add_mobs(conn)
    #del_all_mobs(conn)
    #select_all_mob(conn)


    


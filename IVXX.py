#!/usr/bin/python

# Beast game by Charles Forsyth 2017
# Use and advancement of the IVXX Class

####### Load modules ##########
import subprocess
from subprocess import Popen, PIPE
import time
import os
import sys
import random
import argparse
import ConfigParser
import textwrap
import sqlite3
from sqlite3 import Error

authon = False
#authon = True

class IVXX(object):

	number = 4.2

	def __init__(self,name):
		self.name = name 
		self.output = ""
		return 

	def get_user_input(self,question):
		input = raw_input(question) 
		return input

	def report(self):
                print('Welcome {1} and {0}'.format(str(self.beast_name), str(self.name)))
                print('You have {0} HP, {1} Attack Power, and {2} Defence.'.format(str(self.beast_hp),str(self.beast_atk),str(self.beast_def)))

	def send_output(self,data):
		self.output = data
		print self.output

	def ask_pass(self,thepass):
		if self.get_user_input("Enter the Passphrase: ") == thepass:
			return True
		else:
			return False

	def count_out_loud(self):
		for i in range(int(self.get_user_input("What is the first number? ")),int(self.get_user_input("What is the last number? ")) + 1):
			print i

	def get_weather(self):
		proc=subprocess.Popen('/usr/local/bin/weatherpy', shell=True, stdout=subprocess.PIPE, )
		p1=proc.communicate()[0]
		print p1 
		return p1
		

	def attack(self,hp,atk,df):
	    while hp > 0:
       		 hp = hp - random.randint(1, int(atk))
       		 print(hp)


	def fight(self,bhp,batk,bdef,mhp,matk,mdef):
	    while bhp > 0 and mhp > 0:
	        bhp = int(bhp) - random.randint(1, int(matk)) + int(bdef)
	        mhp = int(mhp) - random.randint(1, int(batk)) + int(mdef)
	        print (bhp,mhp)
	        print (self.select_mob_stat(conn,'name'))
            return bhp,mhp

	def dbfight(self,conn):
            with conn:
                bhp = self.select_character_stat(conn,'hp')
                batk = self.select_character_stat(conn,'atk')
                bdef = self.select_character_stat(conn,'def')
                mhp = self.select_mob_stat(conn,'hp')
                matk = self.select_mob_stat(conn,'atk')
                mdef = self.select_mob_stat(conn,'def')
                hitcount = 0
                while bhp > 0 and mhp > 0:
	            bhp = int(bhp) - random.randint(1, int(matk)) + int(bdef)
	            mhp = int(mhp) - random.randint(1, int(batk)) + int(mdef)
                    #print (bhp,batk,bdef,mhp,matk,mdef)
                    hitcount += 1
                    print ('{0} ---  Beast health:{1} - Mob Health:{2}'.format(hitcount, bhp, mhp))
                #return bhp,mhp

	def logthis(self,name,value):
	    logname = 'log/beast.log'
	    logdata = '{0}:{1}'.format(str(name), str(value))
	    f=open(logname, "a+")
	    f.write("%s\r\n" % (logdata))
	    #print(logdata)
	    f.close()

	def ConfigSectionMap(self,section):
	    dict1 = {}
	    self.options = self.Config.options(section)
	    for option in self.options:
	        try:
	            dict1[option] = self.Config.get(section, option)
	            if dict1[option] == -1:
	                DebugPrint("skip: %s" % option)
	        except:
	            print("exception on %s!" % option)
	            dict1[option] = None
	    return dict1

        def loadconfig(self,charactercfg):
           # charactercfg = "character.cfg"
            self.Config = ConfigParser.ConfigParser()
	    self.Config.read(charactercfg)
	    for self.options in self.Config.sections():
	        self.logthis('options', self.Config.options(self.options))
	    #global beast_name
	    self.beast_name = self.ConfigSectionMap("Main")['name']
	    #global beast_hp
	    self.beast_hp = self.ConfigSectionMap("Main")['hp']
	    #global beast_atk
	    self.beast_atk = self.ConfigSectionMap("Main")['atk']
	    #global beast_def
	    self.beast_def = self.ConfigSectionMap("Main")['def']
 

        def inittime(self):
            self.starttime = time.time() 
            return self.starttime
            


	def menu(self):
		print textwrap.dedent("""\
		### Menu ###
		1. Report
		2. Fight
		3. Database
		q. Quit
		############
		""")
		choice = self.get_user_input("Where to Sir: ")
		if choice == "1":
			self.report()
			self.menu()
		elif choice == "2":
			self.fight(self.beast_hp,self.beast_atk,self.beast_def,100,2,1)	
			self.menu()
		elif choice == "3":
			self.dodatabase()	
			self.menu()
		elif choice == "4":
			self.dodatabase()	
			self.dbfight(self.beast_hp,self.beast_atk,self.beast_def,100,2,1)	
			self.menu()
		elif choice == "q":
			exit()	
		else:
			self.menu()


	def authcheck(self):
		if authon == True:
		        if self.ask_pass("test") == True:
                		pass
        		else:
                		raise RuntimeError('Failed Auth')

	 
 
	def create_connection(self):
	    try:
	        conn = sqlite3.connect(':memory:')
	        return conn
	    except Error as e:
	        print(e)
 
            return None

	def create_table(self,conn,create_table_sql):
	    try:
	        c = conn.cursor()
	        c.execute(create_table_sql)
	    except Error as e:
	        print(e)

	def create_character(self,conn,character):
	    sql = ''' INSERT INTO character(name,hp,atk,def,disc)
	              VALUES(?,?,?,?,?) '''
	    cur = conn.cursor()
	    cur.execute(sql, character)
	    return cur.lastrowid

	def create_mob(self,conn,mob):
	    sql = ''' INSERT INTO mob(name,hp,atk,def,disc)
	              VALUES(?,?,?,?,?) '''
	    cur = conn.cursor()
	    cur.execute(sql, mob)
	    return cur.lastrowid

 
 
	def select_all_character(self,conn):
	    cur = conn.cursor()
	    cur.execute("SELECT * FROM character")
 
	    rows = cur.fetchall()
 
	    for row in rows:
	        print(row)
 
 
	def select_character_stat(self,conn,stat):
	    sql = "SELECT %s FROM character" % stat
	    cur = conn.cursor()
	    cur.execute(sql)
	    rows = cur.fetchall()
	    for row in rows:
	        #print(row[0])
                return row[0]

	def select_mob_stat(self,conn,stat):
	    sql = "SELECT %s FROM mob" % stat
	    cur = conn.cursor()
	    cur.execute(sql)
	    rows = cur.fetchall()
	    for row in rows:
	        #print(row[0])
                return row[0]

	def create_database(self,conn):
	    self.sql_create_character_table = """ CREATE TABLE IF NOT EXISTS character (
	                                        id integer PRIMARY KEY,
	                                        name text NOT NULL,
	                                        hp interger NOT NULL,
	                                        atk interger NOT NULL,
	                                        def interger NOT NULL,
	                                        disc text
	                                    ); """

	    self.sql_create_mob_table = """CREATE TABLE IF NOT EXISTS mob (
	                                        id integer PRIMARY KEY,
	                                        name text NOT NULL,
	                                        hp interger NOT NULL,
	                                        atk interger NOT NULL,
	                                        def interger NOT NULL,
	                                        disc text
		                                );"""

	    if conn is not None:
	        # create character table
	        self.create_table(conn, self.sql_create_character_table)
	        self.create_table(conn, self.sql_create_mob_table)
	        # create mob table
	        #create_table(conn, sql_create_mob_table)
	        #self.characterdetails = ('IVXX', 100, 2, 1, '1st character');
	        self.characterdetails = (self.beast_name, self.beast_hp, self.beast_atk, self.beast_def, '1st character');
	        self.mobdetails = ('Owl', 200, 2, 1, '1st mob');
	        self.character_id = self.create_character(conn, self.characterdetails)
	        self.mob_id = self.create_mob(conn, self.mobdetails)
	    else:
	        print("Error! cannot create the database connection.")

 
 
	def dodatabase(self):

	    conn = self.create_connection()
	    with conn:
	        self.create_database(conn)
	        #select_all_character(conn)
	        #self.select_character_stat(conn,'name')
	        #self.select_mob_stat(conn,'name')
            return conn

	def dbreport(self,conn):

	    with conn:
	        self.select_character_stat(conn,'name')
	        self.select_mob_stat(conn,'name')

 

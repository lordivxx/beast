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
import signal

authon = False
#authon = True

class IVXX(object):

	number = 4.2


	def __init__(self,name,fight_function):
		self.name = name 
		self.fight_function = fight_function 
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
            if int(self.select_character_stat(conn,'hp')) <= 1:
                self.character_dead(conn)
		return
            if random.randint(1,100) == 42:
                id = 4
            else:
                id = random.randint(1, 3)
            print("You hear something!")
            time.sleep(1)
            print(self.select_mob_stat(conn,'name',id))
            time.sleep(1)
            with conn:
                bname = self.select_character_stat(conn,'name')
                bhp = self.select_character_stat(conn,'hp')
                batk = self.select_character_stat(conn,'atk')
                bdef = self.select_character_stat(conn,'def')
                mname = self.select_mob_stat(conn,'name',id)
                mhp = self.select_mob_stat(conn,'hp',id)
                matk = self.select_mob_stat(conn,'atk',id)
                mdef = self.select_mob_stat(conn,'def',id)
                hitcount = 0
                while bhp > 0 and mhp > 0:
	            bhp = int(bhp) - random.randint(1, int(matk)) + int(bdef)
	            mhp = int(mhp) - random.randint(1, int(batk)) + int(mdef)
                    #print (bhp,batk,bdef,mname,mhp,matk,mdef)
                    hitcount += 1
                    print ('{0} ---  Beast health:{1} - {3} Health:{2}'.format(hitcount, bhp, mhp, mname))
                if self.fight_function != 'y':
                    self.update_charcter_stat(conn,'hp',bhp)
                #return bhp,mhp
		if bhp > mhp:
		    print ('{0} wins'.format(bname))
		if mhp > bhp:
		    print ('{0} wins'.format(mname))
                self.commit_db(conn)

	def logthis(self,name,value):
	    logname = './log/beast.log'
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

        def load_character_config(self,charactercfg):
            self.Config = ConfigParser.ConfigParser()
	    self.Config.read(charactercfg)
	    #for self.options in self.Config.sections():
	        #self.logthis('options', self.Config.options(self.options))
	    self.beast_name = self.ConfigSectionMap("Main")['name']
	    self.beast_hp = self.ConfigSectionMap("Main")['hp']
	    self.beast_atk = self.ConfigSectionMap("Main")['atk']
	    self.beast_def = self.ConfigSectionMap("Main")['def']
 
        def load_mob_config(self,mobcfg):
            self.Config = ConfigParser.ConfigParser()
	    self.Config.read(mobcfg)
	    #for self.options in self.Config.sections():
	        #self.logthis('options', self.Config.options(self.options))
	    self.mob_name = self.ConfigSectionMap("Main")['name']
	    self.mob_hp = self.ConfigSectionMap("Main")['hp']
	    self.mob_atk = self.ConfigSectionMap("Main")['atk']
	    self.mob_def = self.ConfigSectionMap("Main")['def']
 

        def inittime(self):
            self.starttime = time.time() 
            return self.starttime
            


	def rmenu(self,conn):
		print("") 
		print("Report:1 Fight:2 Adventure:3 Heal:4 Quit:q") 
                ### Menu ###
		#1. Report
		#2. Fight
		#3. Adventure
		#4. Use small health potion (200 HP)
		#q. Quit
		############
		#""")
		choice = self.get_user_input("Choose: ")
                print("")
		if choice == "1":
                        os.system('clear')
			self.dbreport(conn)
			self.menu(conn)
		elif choice == "2":
                        os.system('clear')
			self.dbfight(conn)	
			self.menu(conn)
		elif choice == "3":
			os.system('clear')
                        self.adventure(conn,10,35)	
			self.menu(conn)
		elif choice == "4":
			os.system('clear')
                        self.visit_healer(conn,200)	
			self.menu(conn)
		elif choice == "q":
                        self.commit_db(conn)
                        self.close_db(conn)
			os.system('clear')
                        exit()	
		else:
			os.system('clear')
                        self.menu(conn)

        def hud(self,conn):
                mob_density = 10
                while True:
                    #print("North:w South:s West:a East:d")
		    print("Report:1 Fight:2 Adventure:3 Heal:4 Quit:q") 
		    choice = self.get_user_input("Choose: ")
		    print("")
                    if choice == "q":
                       self.commit_db(conn)
                       self.close_db(conn)
                       break
                    elif choice == "1":
                       os.system('clear')
                       self.dbreport(conn)
                    elif choice == "2":
                       os.system('clear')
                       self.dbfight(conn)
                    elif choice == "3":
                       os.system('clear')
                       #self.adventure(conn,10,35)
                       self.adventure2(conn)
                    elif choice == "4":
                       os.system('clear')
                       self.visit_healer(conn,200)
                    elif choice == "5":
                       os.system('clear')
                       self.adventure2(conn)



	def authcheck(self):
		if authon == True:
		        if self.ask_pass("test") == True:
                		pass
        		else:
                		raise RuntimeError('Failed Auth')

	 
 
	def create_connection(self):
	    try:
                dbfile = "{0}/repos/beast/beast.db".format(os.environ['HOME'])
	        conn = sqlite3.connect(dbfile)
	        #conn = sqlite3.connect(':memory:')
	        return conn
	    except Error as e:
	        print(e)
 
            return None

        def commit_db(self,conn):
            conn.commit()

        def close_db(self,conn):
            conn.close()

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
 
 
	def update_charcter_stat(self,conn,stat,statupdate):
	    sql = "UPDATE character SET %s = %s " % (stat,statupdate)
	    cur = conn.cursor()
	    cur.execute(sql)

	def visit_healer(self,conn,statupdate):
            self.update_charcter_stat(conn,'hp',statupdate)

	def select_character_stat(self,conn,stat):
	    sql = "SELECT %s FROM character" % stat
	    cur = conn.cursor()
	    cur.execute(sql)
	    rows = cur.fetchall()
	    for row in rows:
	        #print(row[0])
                return row[0]

	def select_mob_stat(self,conn,stat,id):
	    sql = "SELECT %s FROM mob WHERE id = %s" % (stat,id)
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
	        self.characterdetails = (self.beast_name, self.beast_hp, self.beast_atk, self.beast_def, '1st character');
	        self.mobdetails = (self.mob_name, self.mob_hp, self.mob_atk, self.mob_def, '1st mob');
	        self.character_id = self.create_character(conn, self.characterdetails)
	        self.mob_id = self.create_mob(conn, self.mobdetails)
                self.commit_db(conn)
	    else:
	        print("Error! cannot create the database connection.")

 
 
	def dbreport(self,conn):

	    #with conn:
            print('Username: {1} and Beast: {0}'.format(str(self.select_character_stat(conn,'name')), str(self.name)))
            print('{3} has {0} HP, {1} Attack Power, and {2} Defence.'.format(int(self.select_character_stat(conn,'hp')),int(self.select_character_stat(conn,'atk')),int(self.select_character_stat(conn,'def')),str(self.select_character_stat(conn,'name'))))
            #print('There is a {3} in the area with {0} HP, {1} Attack Power, and {2} Defence.'.format(int(self.select_mob_stat(conn,'hp')),int(self.select_mob_stat(conn,'atk')),int(self.select_mob_stat(conn,'def')),str(self.select_mob_stat(conn,'name'))))
	        #self.select_character_stat(conn,'name')
	        #self.select_mob_stat(conn,'name')

        def check_for_action(self,percent):
            action_is_go = 0
            if random.randint(0,100) < percent:
                action_is_go = 1
                return action_is_go
            return action_is_go

        def adventure(self,conn,adv_time_lenght,mob_density):
            adv_time = 1
            self.clear_terminal()
            while adv_time != adv_time_lenght:
                if int(self.select_character_stat(conn,'hp')) <= 1:
                    self.character_dead(conn)
                    return

                if self.check_for_action(int(mob_density)) == 1:
                    #print("You hear something!")
                    #time.sleep(2)
                    #print(self.mob_name)
                    #time.sleep(2)
                    self.dbfight(conn)

                #print(self.check_for_action(5))
                print('\ \\')
                if self.check_for_action(int(1)) == 1: 
                    self.visit_healer(conn,200)
                    print('{0} finds a potion of revenenation and drinks it.'.format(str(self.select_character_stat(conn,'name'))))
                    print('Your beast now has {0} HP, {1} Attack Power, and {2} Defence.'.format(int(self.select_character_stat(conn,'hp')),int(self.select_character_stat(conn,'atk')),int(self.select_character_stat(conn,'def'))))
                    print(':')
                
                
                print('/ /')
                    
                time.sleep(1)
                adv_time += 1
        
        def get_room_id(self,conn,geoidy,geoidx):
            sql = "SELECT {0} FROM {1} WHERE geoidy={2} AND geoidx={3}".format('id','adv1_map',geoidy,geoidx)
            #print(sql)
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            for row in rows:
                #print(row[0])
                return row[0]
 
        def get_room_stat_by_id(self,conn,roomid,stat):
            sql = "SELECT {0} FROM {1} WHERE id={2}".format(str(stat),'adv1_map',roomid)
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            for row in rows:
                #print(row[0])
                return row[0]
 

        def adventure2(self,conn):
            self.clear_terminal()
            print("""
            
            
            
            
    Welcome to the 1st Beast Adventure  

            





            """)

            self.loc = [0,0]
	    self.roomid = self.get_room_id(conn,self.loc[0],self.loc[1])
	    self.room_run_script(conn,self.roomid)
            #roomid = self.get_room_id(conn,self.loc[0],self.loc[1])
            while True:
		self.roomid = self.get_room_id(conn,self.loc[0],self.loc[1])
		#self.room_run_script(conn,self.roomid)
                print("North:w South:s West:a East:d") 
                print("Status:status Heal:heal Train:t Town:qq")
                choice = self.get_user_input("Choose: ")
                print("")
                if choice == "w":
                   os.system('clear')
                   print("moving North")
                   #print(self.loc)
                   loc_check = [self.loc[0],self.loc[1] + 1]
                   if self.get_room_id(conn,loc_check[0],loc_check[1]):
                        self.loc = [self.loc[0],self.loc[1] + 1]
		        self.roomid = self.get_room_id(conn,self.loc[0],self.loc[1])
                        self.room_run_script(conn,self.roomid)
                   else:
                        self.report_edge() 

                elif choice == "s":
                   os.system('clear')
                   print("moving South")
                   #print(self.loc)
                   loc_check = [self.loc[0],self.loc[1] - 1]
                   if self.get_room_id(conn,loc_check[0],loc_check[1]):
                        self.loc = [self.loc[0],self.loc[1] - 1]
		        self.roomid = self.get_room_id(conn,self.loc[0],self.loc[1])
                        self.room_run_script(conn,self.roomid)
                   else:
                        self.report_edge() 
 
                elif choice == "a":
                   os.system('clear')
                   print("moving West")
                   #print(self.loc)
                   loc_check = [self.loc[0] - 1,self.loc[1]]
                   if self.get_room_id(conn,loc_check[0],loc_check[1]):
                        self.loc = [self.loc[0] - 1,self.loc[1]]
		        self.roomid = self.get_room_id(conn,self.loc[0],self.loc[1])
                        self.room_run_script(conn,self.roomid)
                   else:
                        self.report_edge() 
 
                elif choice == "d":
                   os.system('clear')
                   print("moving East")
                   #print(self.loc)
                   loc_check = [self.loc[0] + 1,self.loc[1]]
                   if self.get_room_id(conn,loc_check[0],loc_check[1]):
                        self.loc = [self.loc[0] + 1,self.loc[1]]
		        self.roomid = self.get_room_id(conn,self.loc[0],self.loc[1])
                        self.room_run_script(conn,self.roomid)
                   else:
                        self.report_edge() 
                elif choice == "town":
                   os.system('clear')
                   self.commit_db(conn)
                   break
                elif choice == "qq":
                   os.system('clear')
                   self.commit_db(conn)
                   break
                elif choice == "heal":
                   self.visit_healer(conn,200)
                   self.commit_db(conn)
                elif choice == "status":
                   self.dbreport(conn)
                   self.commit_db(conn)
                elif choice == "train":
                   self.train_gen(conn)
                   self.commit_db(conn)
                elif choice == "t":
                   self.train_gen(conn)
                   self.commit_db(conn)
 
            #self.room_run_script(conn,roomid)

        def report_edge(self):
            print("""
                        
                       

      This is the edge of the map
                        
                        
                        
                        
            """)
            
            

        def room_run_script(self,conn,roomid):
            #print(roomid)
            #print(self.get_room_stat_by_id(conn,self.roomid,'disc'))
            self.room_welcome(conn,self.get_room_stat_by_id(conn,self.roomid,'disc'))
            time.sleep(2)


            if int(self.select_character_stat(conn,'hp')) <= 1:
                self.character_dead(conn)
                return

            if self.check_for_action(int(self.get_room_stat_by_id(conn,self.roomid,'mobden'))) == 1:
               self.dbfight(conn)

            #print(self.check_for_action(5))
            #print('\ \\')
            #if self.check_for_action(int(1)) == 1: 
            #    self.visit_healer(conn,200)
            #    print('{0} finds a potion of revenenation and drinks it.'.format(str(self.select_character_stat(conn,'name'))))
            #    print('Your beast now has {0} HP, {1} Attack Power, and {2} Defence.'.format(int(self.select_character_stat(conn,'hp')),int(self.select_character_stat(conn,'atk')),int(self.select_character_stat(conn,'def'))))
            #    print(':')
            
        def room_welcome(self,conn,roomdisc):
            print("""



      {0}
      
      
      
      
      
            """.format(roomdisc))
        def clear_terminal(self):
            os.system('clear')

        def character_dead(self,conn):
            print('{0} has become too weak and must return to town.'.format(str(self.select_character_stat(conn,'name'))))
            #self.hud(conn)
            #RETURN false
        
        def current_location(self,conn):
            return self.loc

        def train_gen(self,conn):
            adv_time = 1
            adv_time_lenght = self.get_user_input("How many sec to Train?: ")
            mob_density = self.get_user_input("Mob density 1-100: ")
            self.fight_function = 'y'
            self.clear_terminal()
            while adv_time != int(adv_time_lenght):
                if int(self.select_character_stat(conn,'hp')) <= 1:
                    self.character_dead(conn)
                    return

                if self.check_for_action(int(mob_density)) == 1:
                    #print("You hear something!")
                    #time.sleep(2)
                    #print(self.mob_name)
                    #time.sleep(2)
                    self.dbfight(conn)

                #print(self.check_for_action(5))
                print('\ \\')
                if self.check_for_action(int(1)) == 1: 
                    self.visit_healer(conn,200)
                    print('{0} finds a potion of revenenation and drinks it.'.format(str(self.select_character_stat(conn,'name'))))
                    print('Your beast now has {0} HP, {1} Attack Power, and {2} Defence.'.format(int(self.select_character_stat(conn,'hp')),int(self.select_character_stat(conn,'atk')),int(self.select_character_stat(conn,'def'))))
                    print(':')
                
                
                print('/ /')
                    
                time.sleep(.5)
                adv_time += 1
            

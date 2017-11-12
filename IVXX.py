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
            return bhp,mhp

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

        def loadconfig(self):
            self.charactercfg = "character.cfg"
            self.Config = ConfigParser.ConfigParser()
	    self.Config.read(self.charactercfg)
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

	 


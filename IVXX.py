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
import libbeast

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

	def greet(self):
		print "\n" * 10
		print "Welcome " + self.name + " would you like to play a game? "		

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


	def fight(self,bhp,batk,mhp,matk):
	    while bhp > 0 and mhp > 0:
	        bhp = int(bhp) - random.randint(1, int(matk))
	        mhp = int(mhp) - random.randint(1, int(batk))
	        print (bhp,mhp)

	def logthis(self,name,value):
	    logname = 'log/beast.log'
	    logdata = '{0}:{1}'.format(str(name), str(value))
	    f=open(logname, "a+")
	    f.write("%s\r\n" % (logdata))
	    #print(logdata)
	    f.close()

	def ConfigSectionMap(self,section):
	    dict1 = {}
	    options = Config.options(section)
	    for option in options:
	        try:
	            dict1[option] = Config.get(section, option)
	            if dict1[option] == -1:
	                DebugPrint("skip: %s" % option)
	        except:
	            print("exception on %s!" % option)
	            dict1[option] = None
	    return dict1

        def inittime(self):
            self.starttime = time.time() 
            return self.starttime
            


	def menu(self):
		print textwrap.dedent("""\
		### Menu ###
		1. Count
		2. Ask Pass
		3. Greet
		4. Report Status
		q. Quit
		############
		""")
		choice = self.get_user_input("Where to Sir: ")
		if choice == "1":
			self.count_out_loud()
		elif choice == "2":
			if self.ask_pass("test") == True:
				print "You Pass!" 
			else:
				print "Incorrect Sir!! I bid you Good Day!"
		elif choice == "3":
			self.greet()
		elif choice == "4":
			print "\n" * 20
			print "Gathering data now ..."
			print "\n" * 20
			self.fight(100,2,100,2)	
		elif choice == "q":
			exit()	
		else:
			x.menu()


	def authcheck(self):
		if authon == True:
		        if self.ask_pass("test") == True:
                		pass
        		else:
                		raise RuntimeError('Failed Auth')

	 


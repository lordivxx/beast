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


class map(object):
    def __init__(self):
        self.mapvalue = 42 

    def current_location(self):
       print(self.loc) 

    def move_north(self):
        self.loc = [self.loc[0],self.loc[1] + 1]
        
class room(map):
     
    def __init__(self,geoid,name,room_discription):
        super(room, self).__init__()
        self.geoid = geoid
        self.name = name
        self.room_discription = room_discription
        self.loc = geoid

    def look(self):
        print("You look around")
        print(self.room_discription)
        

#class forest(area):

#    def __init__(self,name):
#        super(forest, self).__init__()
#        self.loc = [1,0] 
#        self.name = name


basecamp = room([0,0],"Base Camp","Begining area of the 1st adventure. There is only a small tent and a campfire still burning.")
geoid_01 = room([0,1],"Room 0 1","You are in the north woods")
geoid_0m1 = room([0,-1],"Room 0 1","You are in the south woods")
geoid_10 = room([1,0],"Room 1 0","You are in the East woods")
geoid_m10 = room([-1,0],"Room -1 0","You are in the West woods")
#f10 = forest("f10")
print(basecamp.geoid, basecamp.current_location())
#print(q10.loc, q10.current_location())
basecamp.move_north()
print(basecamp.geoid, basecamp.current_location())
print(geoid_01.look())


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



###### setting argument requierments with ArgParse 
parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-c", "--charactercfg" , help='The path to a character config file', required=False)
args = parser.parse_args()


######## Assign Variables  ######
charactercfg = args.charactercfg
if charactercfg == None:
    charactercfg = "character.cfg"
print(charactercfg)
######## Functions #########


########## Main Code ##########
if __name__ == '__main__':
    # Load the class
    x = IVXX(os.environ['USER'])
    ## Start timing
    x.inittime()
    x.logthis('commandline', sys.argv)


    #x.fight(beast_hp,beast_atk,100,2)
    x.loadconfig(charactercfg)
    x.report()

    x.authcheck()
    conn = x.dodatabase()
    x.dbreport(conn)
    x.dbfight(conn)
    #x.menu()


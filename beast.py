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
requiredNamed.add_argument("-m", "--mobcfg" , help='The path to a mob config file', required=False)
requiredNamed.add_argument("-d", "--dbinit" , help='Init the db', required=False)
requiredNamed.add_argument("-i", "--interactive" , help='interactive', required=False)
requiredNamed.add_argument("-f", "--fight_function" , help='fight_function', required=False)
args = parser.parse_args()


######## Assign Variables  ######
charactercfg = args.charactercfg
if charactercfg == None:
    charactercfg = "character.cfg"
mobcfg = args.mobcfg
if mobcfg == None:
    mobcfg = "mob.cfg"

dbinit = args.dbinit
interactive = args.interactive
fight_function = args.fight_function
if fight_function == None:
    fight_unction = 'n'
######## Functions #########


########## Main Code ##########
if __name__ == '__main__':
    
    # Load the class
    x = IVXX(os.environ['USER'],fight_function)


    ## Start timing
    x.inittime()
    x.logthis('commandline', sys.argv)


    x.load_mob_config(mobcfg)
    x.load_character_config(charactercfg)
    #x.report()

    x.authcheck()
    conn = x.create_connection()
    if dbinit == 'y':
        x.create_database(conn)
        x.commit_db(conn)
        x.close_db(conn)
        exit()
    if interactive == 'y':
        x.menu(conn)
        exit()
    x.dbreport(conn)
    #x.dbfight(conn)
    #x.update_charcter_stat(conn,'hp',100)
    x.adventure(conn,10)
    x.dbreport(conn)
    x.close_db(conn)

    #x.menu()


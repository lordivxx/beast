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



###### setting argument requierments with ArgParse 
parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-c", "--charactercfg" , help='The path to a character config file', required=False)
requiredNamed.add_argument("-m", "--mobcfg" , help='The path to a mob config file', required=False)
requiredNamed.add_argument("-d", "--dbinit" , help='Init the db', required=False)
requiredNamed.add_argument("-i", "--interactive" , help='broken', required=False)
requiredNamed.add_argument("-f", "--fight_function" , help='y = beast does not update the database for the player at the end of the fight', required=False)
args = parser.parse_args()


######## Assign Variables  ######
charactercfg = args.charactercfg
if charactercfg == None:
#    charactercfg = "/rhome/forsythc/.character.cfg"
    charactercfg = "./character.cfg"
mobcfg = args.mobcfg
if mobcfg == None:
    #mobcfg = "/rhome/forsythc/.mob.cfg"
    mobcfg = "./mob.cfg"

dbinit = args.dbinit
interactive = args.interactive
fight_function = args.fight_function
if fight_function == None:
    fight_function = 'n'
######## Functions #########


def signal_handler(signal, frame):
    #print('Beast is closed!')
    print('')
    sys.exit(0)



########## Main Code ##########
if __name__ == '__main__':
    
    # Load the class
    #x = IVXX(os.environ['USER'],fight_function)
    x = IVXX("ivxx",fight_function)
    signal.signal(signal.SIGINT, signal_handler)


    ## Start timing
    x.inittime()
    #x.logthis('commandline', sys.argv)


    #x.load_mob_config(mobcfg)
    #x.load_character_config(charactercfg)
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
    #x.dbreport(conn)
    #x.dbfight(conn)
    #x.update_charcter_stat(conn,'hp',100)
    #x.adventure(conn,120,5)
    #x.select_mob_stat(conn,'name',1)
    x.print_beast_title()
    x.dbreport(conn)
    x.hud(conn)
    x.close_db(conn)

    #x.menu()


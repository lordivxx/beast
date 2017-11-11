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



###### setting argument requierments with ArgParse 
parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-c", "--charactercfg" , help='The path to a character config file', required=False)
args = parser.parse_args()


######## Assign Variables  ######
charactercfg = args.charactercfg


######## Functions #########
def attack(hp,atk,df):
    while hp > 0:
        hp = hp - random.randint(1, int(atk))
        print(hp)


def fight(bhp,batk,mhp,matk):
    while bhp > 0 and mhp > 0:
        bhp = int(bhp) - random.randint(1, int(matk))
        mhp = int(mhp) - random.randint(1, int(batk))
        print (bhp,mhp)

def logthis(name,value):
    logname = 'log/{0}.log'.format(int(starttime))
    logdata = '{0}:{1}'.format(str(name), str(value))
    f=open(logname, "a+")
    f.write("%s\r\n" % (logdata))
    #print(logdata)
    f.close()

def ConfigSectionMap(section):
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


########## Main Code ##########
if __name__ == '__main__':
    ## Start timing
    starttime = time.time()
    logthis('commandline', sys.argv)

    ## Reads in the config file that was givin and stores some values from it
    Config = ConfigParser.ConfigParser()
    Config.read(charactercfg)
    for options in Config.sections():
        logthis('options', Config.options(options))
    beast_name = ConfigSectionMap("Main")['name']
    beast_hp = ConfigSectionMap("Main")['hp']
    beast_atk = ConfigSectionMap("Main")['atk']
    beast_def = ConfigSectionMap("Main")['def']
    print('Welcome Back {0}'.format(str(beast_name)))
    print('You have {0} HP, {1} Attack Power, and {2} Defence.'.format(str(beast_hp),str(beast_atk),str(beast_def)))
    #attack(int(beast_hp),int(beast_atk),int(beast_def))
    fight(beast_hp,beast_atk,100,2)

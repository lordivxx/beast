#! /usr/bin/python


# Beast game by Charles Forsyth 2017

####### Load modules ##########
import subprocess
from subprocess import Popen, PIPE
import time
import os
import sys
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
def logthis(name,value):
    logname = 'beast_{0}.log'.format(int(starttime))
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
    print(Config.sections())
    print(Config.options("Main"))
    beast_name = ConfigSectionMap("Main")['name']
    print(beast_name)

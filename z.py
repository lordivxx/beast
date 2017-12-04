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
from map import map

#print("hi")

x = map()

#print(map.map().tester())
#print(x.tester("yo"))
print(x.current_location())

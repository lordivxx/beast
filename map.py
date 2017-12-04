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


class map:
    location = "really"
    def __INIT__(self, location):
        self.location = "test" 
        location = "ok then"

    def tester(self,what):
        print(what)
        print(self.location)

    def current_location(self):
        location = [0,0]
        print(location)

""" The main file to begin execution of the automation.
It all starts with traverse.py, from this file, we pass it arguments, and it then takes care of the rest.  """
import os
import platform
import sys
import shutil
import argparse
import warnings
from datetime import datetime
from os.path import realpath, dirname
from utilities.json_helper import LoadJson, GetJsonValue, WriteJsonFile

PARSER = argparse.ArgumentParser(
    description='''Computerization is a test framework for webui, api and mobile testing''')
PARSER.add_argument('-R'
                    , '--regression'
                    , help='Runs all regression tests found in the regreession test json file.'
                    , action='store_true')

PARSER.add_argument('-L',
                    '--local',
                    help='Runs all the regression test on local machine',
                    action='store_true')

PARSER.add_argument('-G'
                    , '--generate'
                    , type=str
                    , help='Creates a new traverse config with default settings.')

PARSER.add_argument('-BS',
                    '--browser stack',
                    help='Runs all the regression test on browser stack')

# Read arguments from the CMD
ARGS = PARSER.parse_args()





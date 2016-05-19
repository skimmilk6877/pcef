#-*- coding: utf-8 -*-
#!/usr/bin/python

 
#2016-03-23  sunhao

#############package import##############

import os
import sys
from commands import getstatusoutput


##################Script static parameters (including the relative positions of folders, etc.)##################
#Script directory
PWD = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
SCRIPT_DIR = PWD[:PWD.rfind("/")]

TEST_FILE=PWD + '/TEST'


#################Script dynamic parameters#############################
TASK_LIST_FILE=PWD + '/TASK_LIST'

MIRROR_PARALLEL_SMALL=20


SOFTWARE_BASE='/opt'


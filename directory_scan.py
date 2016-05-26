#-*- coding: utf-8 -*-
#!/usr/bin/python



#2016-03-23  sunhao



import os
import sys

#from commands import getstatusoutput


#import gcware

##################Script static parameters (including the relative positions of folders, etc.)##################
#Script directory
PWD = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
SCRIPT_DIR = PWD[:PWD.rfind("/")]


#################Script dynamic parameters#############################
DATABASE_BASE_DIR='/opt'


class GDrectory():


    def __init__(self,base_dir):
        self.base_dir = base_dir
        self.gc_datadir = self.base_dir + '/gcluster/userdata/gcluster'
        self.gn_datadir = self.base_dir + '/gnode/userdata/gbase'

        

gbase_dir = GDrectory(DATABASE_BASE_DIR)   


print gbase_dir.base_dir
print gbase_dir.gc_datadir
print gbase_dir.gn_datadir
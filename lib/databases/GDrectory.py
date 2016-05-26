#-*- coding:UTF-8 -*-
#!/usr/bin/python




class GDrectory():


    def __init__(self,basedir):
        self.basedir = basedir
        self.gc_datadir = self.basedir + '/gcluster/userdata/gcluster'
        self.gn_datadir = self.basedir + '/gnode/userdata/gbase'

    range
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 00:08:08 2014

@author: Abdelouahab
"""


import fileinput
import argparse
import time
import datetime


parser = argparse.ArgumentParser()
parser.add_argument('hash', help='The hash you provide')
parser.add_argument('dictionnary', help='The dictionnary that contains the list of the hashs')
args = parser.parse_args()

resul = ''

try:
    begin = time.time()
    for line in fileinput.input('{0}'.format(args.dictionnary)):
        if args.hash == line[18:-2]:
            resul =  line[1:16]            
    end = time.time() - begin
    fileinput.close()
    
    print 'End of the operation, ended at {0}, took {1} seconds'.format(str(datetime.datetime.now())[:19], end)
    if resul:
        print 'Hohohooh! we found it, your word is: ' + resul
    else:
        print 'Ooops! Nothing found'

except IOError:
    print 'Bzzzzz! this file dont exist -_-'

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 17:51:48 2014

@author: Abdelouahab
"""
import fileinput
import argparse
import time
import datetime
import hashlib



result = []
parser = argparse.ArgumentParser()
parser.add_argument('binary', help='File containing your binaries')
parser.add_argument('input', help='Your input file')
parser.add_argument('begin', help='The range where your iterations begin, example 0, 10, 1000, 4332240...etc')
parser.add_argument('step', help='The step that will be used in the range, if step = 100, then xrange(0, 100), the last element is excluded (here we got from 0 to 99)')
parser.add_argument('output', help='Your output file')
args = parser.parse_args()

debut = time.time()

for binary in fileinput.FileInput('{0}'.format(args.binary)):
    r=''
    for line in fileinput.FileInput('{0}'.format(args.input)):
        for i in xrange(int(args.begin), int(args.step)):
            r = str(i).rjust(10, '0') if len(r)<11 else r[:-1]
            if line[:-1] == hashlib.md5(args.binary+r).hexdigest():
                result.append((line[:-1], r, '\n')) 
    fileinput.close()
    del r
    fin = time.time() - debut
    
    with open('{0}{1}.txt'.format(args.output, binary[:-1]), 'w') as f:
        f.write('Operation ended at {0}, took {1} seconds.\nYou got {2} results, here is your list: {3}'.format(str(datetime.datetime.now())[:19], fin, len(result), result))

fileinput.close()
f.close()

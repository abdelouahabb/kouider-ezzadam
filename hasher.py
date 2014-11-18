# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 23:01:24 2014

@author: Abdelouahab
"""

import hashlib
import argparse


r = ''

parser = argparse.ArgumentParser()
parser.add_argument('binary', help='Use one binary here')
parser.add_argument('begin', help='The range where your iterations begin, example 0, 10, 1000, 4332240...etc')
parser.add_argument('step', help='The step that will be used in the range, if step = 100, then xrange(0, 100), the last element is excluded (here we got from 0 to 99)')
parser.add_argument('output', help='Your output file')
args = parser.parse_args()

with open('{0}'.format(args.output), 'w') as destine:  
    for i in xrange(int(args.begin), int(args.step)):
        r = str(i).rjust(10, '0') if len(r)<11 else r[:-1]
        destine.write('({0}, {1})\n'.format(args.binary+r, hashlib.md5(args.binary+r).hexdigest()))

destine.close()

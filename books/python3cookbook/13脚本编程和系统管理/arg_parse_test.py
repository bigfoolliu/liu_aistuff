#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
查看结果
python3 3.py -h
"""

import argparse


parser = argparse.ArgumentParser(prog="Test Prog", description="Prog for testing argparse")

parser.add_argument(dest='filenames', metavar='filename', nargs='*')
parser.add_argument('-p', '--pat', metavar='pattern', required=True, dest='patterns', action='append', help='text pattern to search for')
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
parser.add_argument('-o', dest='outfile', action='store', help='output file')
parser.add_argument('--speed', dest='speed', action='store', choices={'slow','fast'}, default='slow', help='search speed')

args = parser.parse_args()

# Output the collected arguments
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)

#!/usr/bin/env python3

import argparse
import mcb185
import random

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?

# setup
parser = argparse.ArgumentParser(description='explore open reading frame length.')
# required arguments
#none
# optional arguments with default parameters
parser.add_argument('--size', required=False, type=int, default=4500000,
	metavar='<str>', help='genome size [%(default)i]')
parser.add_argument('--orfmin', required=False, type=int, default=100,
	metavar='<int>', help='minimum open reading frame length [%(default)i]')
parser.add_argument('--gc', required=False, type=float, default=0.5,
	metavar='<float>', help='gc fraction [%(default).3f]')
# switches
parser.add_argument('--info', action='store_true',
	help='provide additional info')
parser.add_argument('--seed', action='store_true',
	help='fix random seed')
# finalization
arg = parser.parse_args()

#get same random numbers every time you run the program
if arg.seed: random.seed(1)

if arg.info: print('genome size:', arg.size, 'min orf:', arg.orfmin, 'GC%:', arg.gc)

#generate random genome of specified size, GC composition
seq = mcb185.randseq(arg.size, arg.gc)
#print(seq)

#look for ORFs
orfs = []
for n in mcb185.findorfs(seq):
	if n > arg.orfmin:
		orfs.append(n)
print('number of orfs present:', len(orfs)) #aa lengths > orfmin (100aa)

#histogram- how many counts at each length
orfs.sort()
lengths = []
tallies = []
for i in orfs:
	if i not in lengths: 
		lengths.append(i)
		counts = orfs.count(i)
		tallies.append(counts)

print('histogram of ORF lengths:)
print('lengths:', 'count:')
for length, tally in zip(lengths, tallies): print(length, '\t', tally)






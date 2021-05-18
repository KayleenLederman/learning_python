#!/usr/bin/env python3

import argparse
import mcb185
from statistics import mean, median

# Write a program that computes statistics about a fasta file
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length
# Use argparse
# Make useful functions and add them to your library


# setup
parser = argparse.ArgumentParser(description='stats about sequence.')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='required fasta file')


# finalization
arg = parser.parse_args()

length = []
for name, seq in mcb185.read_fasta(arg.file):
	#print (name, len(seq))
	length.append(len(seq))
length.sort()


print('number of sequences is:', len(length))
print('min is:', length[0])
print('max is:', length[-1])
print('mean is:', mean(length))
print('median is:', median(length))
print('N50 is:', mcb185.n50(length))
	
#sum = 0
#for value in length:
	#sum += value
#print('sum is:', sum)
#print(sum(length))  #easy way to get sum using functions in python






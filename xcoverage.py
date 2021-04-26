#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average depth
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome (1 read length on either end)

import sys
import random
coverage = []
genome_size = int(sys.argv[1])
read_number = int(sys.argv[2])
read_length = int(sys.argv[3])

#populate empty list with genome_size number of 0s
for i in range(genome_size):
	coverage.append(0)
	
#populate coverage list with random reads at random positions, add 1 for each hit
for i in range(read_number):
	start = random.randint(0, genome_size - read_length)
	for j in range(read_length):
		coverage[start + j] += 1
#print(coverage)

# Minimum/Maximum
min = coverage[read_length] #compare each value to previous value and see if it's higher/lower
max = coverage[read_length]
total = 0
for v in coverage[read_length: -read_length]:
	if v < min: min = v
	if v > max: max = v
	total += v				#add up all values in coverage (excluding ends) for total read depth

print('Min:', min, 'Max:', max, 'Avg. Read Depth:', total/(genome_size - 2 * read_length))



#put read at random position
#start = random.randint(0, (int(len(genome_size) - read_length)))
#read = genome_size[start: start + read_length]
#print(start)
#print(read)

#create read_number amount of read lengths at random positions

	

"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""

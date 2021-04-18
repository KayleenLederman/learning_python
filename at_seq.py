#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

t = 0.6
seq = ''
at = 0

for nt in range(30):			
	p = random.random()
	if p < t:
		if random.random() < 0.5: seq += 'A' 
		else:                     seq += 'T' 
		at += 1
	else:
		if random.random() < 0.5: seq += 'G'
		else:                     seq += 'C'
at_fraction = at/len(seq)

print(len(seq), at_fraction, seq)

"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""

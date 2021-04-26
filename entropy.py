#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi)) pi = probability of i
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

#print(sys.argv)
p =[] #probability
#for i in range(1, len(sys.argv)):
	#p.append(float(sys.argv[i]))
#print(p)

#add values from command line to list and convert to floats
for s in sys.argv[1: ]:
	p.append(float(s))

# make sure all p values inputted add up to one
#if (sum(p)) != 1 #can't do b/c floating point values don't have enough precision
assert(math.isclose(sum(p), 1, abs_tol = 0.2)) 
		
H = 0
for i in range(len(p)):
	H -= (p[i] * math.log2(p[i])) #negative sum
print(f'{H:.3f}')
"""
python3 entropy.py 0.1 0.2 0.3 0.4
1.846
"""

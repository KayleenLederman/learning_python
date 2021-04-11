#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

# your code goes here
	
start = 0
end = 3
for c in range(len(dna)//3):
	print(dna[start:end])
	start = start + 3
	end = end + 3
k = 4	
for f in range(k):	
	print(f)
	for i in range(f, len(dna)-k + 1, k):
		print(dna[i: i +k])
	

	
"""
python3 codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""

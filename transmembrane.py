#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa



def kd(seq):   #avg kyte doolittle hydrophobicity of a given sequence
	kdtot = 0
	for aa in seq:
		if   aa == 'I': kdtot += 4.5
		elif aa == 'V': kdtot += 4.2
		elif aa == 'L': kdtot += 3.8
		elif aa == 'F': kdtot += 2.8
		elif aa == 'C': kdtot += 2.5
		elif aa == 'M': kdtot += 1.9
		elif aa == 'A': kdtot += 1.8
		elif aa == 'G': kdtot -= 0.4
		elif aa == 'T': kdtot -= 0.7
		elif aa == 'S': kdtot -= 0.8
		elif aa == 'W': kdtot -= 0.9
		elif aa == 'Y': kdtot -= 1.3
		elif aa == 'P': kdtot -= 1.6
		elif aa == 'H': kdtot -= 3.2
		elif aa == 'E': kdtot -= 3.5
		elif aa == 'Q': kdtot -= 3.5
		elif aa == 'D': kdtot -= 3.5
		elif aa == 'N': kdtot -= 3.5
		elif aa == 'K': kdtot -= 3.9
		elif aa == 'R': kdtot -= 4.5
	kdavg = kdtot/len(seq)
	return kdavg
	
#ex = 'DNKR'
#print(kd(ex))
	

#get all sequences:
ids = []
proteins = []
with open(sys.argv[1]) as fp:  #input file name used into command line
	seq = []
	for line in fp.readlines():
		line = line.rstrip()  #remove excess spaces
		if line.startswith('>'):  #print lines that start with ">"
			words = line.split() #splits lines at spaces
			ids.append(words[0][1:])  #only return identifier seq instead of whole line, exclude >
			if len(seq) > 0: proteins.append("".join(seq)) 
			seq = []
		else: 
			seq.append(line)
	proteins.append("".join(seq)) #adds last remaining protein seq that isn't followed by >
#print(len(ids), len(proteins))			


#signal peptide
def signal(sequence, w):
	for i in range(30 - w + 1):
		window = sequence[i: i + w]
		if kd(window) > 2.5: return True
	return False

#hydrophobic region
def hydro(sequence, w):
	for i in range(30, len(sequence) - 1):
		pcheck = False
		window = sequence[i: i + w]
		for aa in window:
			if aa == 'P': pcheck = True 
		if kd(window) > 2.0 and pcheck == False: return True
	return False
	
#proline check
def hasprolines(sequence):
	for aa in sequence:
		if aa == 'P': return True
	return False

#hydrophobic alpha helix (hah)
def hah(seq, w, t):
	for i in range(len(seq) - w + 1):
		window = seq[i: i + w]
		if kd(window) > t and not hasprolines(window): 
			return True	
	return False
	
#def sigpep(seq):
	#return hah(seq, 8, 2.5)
	
#def transmemb(seq):
	#return hah(seq, 11, 2)
		
for id, protein in zip(ids,proteins):
	n_term = protein[:30]
	c_term = protein[30: -1]
	if hah(n_term, 8, 2.5) and hah(c_term, 11, 2): print(id)
	#if sigpep(n_term) and transmemb(c_term): print(id)



"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""

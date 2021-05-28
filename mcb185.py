import random

#returns list with identifier and sequence from fasta file
def read_fasta(filename):
	name = None
	seq = []
	
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			elif line.startswith('>'):
				if len(seq) > 0: # now is the time to return name, seq
					yield name, ''.join(seq)
				words = line.split()
				name = words[0][1:]
				seq = []
			else:
				line = line.rstrip()
				seq.append(line)
	yield name, ''.join(seq)


def gc(dna):
	g = dna.count('G')
	c = dna.count('C')
	return (g + c)/len(dna)
	
	
#N50- sum values, once its great than 1/2 of total sum, that is N50
def n50(length):
	length.sort()
	running_sum = 0
	total = sum(length)
	for value in length:
		running_sum += value
		if running_sum > total/2: 
			return value
			break

#create random sequence of random length and gc composition			
#seq = mcb185.randseq(arg.size, arg.gc)
def randseq(length, gc):
	seq = ''
	for i in range(length):
		if random.random() < gc: 
			seq += random.choice('GC')
		else: 
			seq += random.choice('AT')
	return seq

	
#orf lengths in seq
def findorfs(seq):
	lengths = []
	for i in range(len(seq) - 2):
		start = None
		stop = None
		if seq[i: i + 3] == 'ATG':
			start = i
			for j in range(i, len(seq) - 2, 3):
				codon = seq[j: j + 3]
				if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
					stop = j
					break
		if stop != None: lengths.append((stop - start)/3)
	return lengths

#orfs
def orfseqs(seq):
	orfseqs = []
	for i in range(len(seq) - 2):
		start = None
		stop = None
		if seq[i: i + 3] == 'ATG':
			start = i
			for j in range(i, len(seq) - 2, 3):
				codon = seq[j: j + 3]
				if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
					stop = j
					break
		if stop != None: orfseqs.append(seq[start: stop])
	return orfseqs

#translate dna seqs into protein
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

def translate(seq):
	seq = seq.upper() #makes sure all letters are upper so that both upper and lowercase letters are translated
	protein = ''
	for i in range(0, len(seq) -2, 3):
		codon = seq[i: i + 3]
		if codon in gcode: 
			protein += gcode[codon]
		else: 
			protein += 'X'  #any codon not in dictionary will become X
	return protein

#return reverse complement of DNA seq
def anti(dna):
	seq = ''
	for c in dna[::-1]:
		if   c == 'A': seq += 'T'
		elif c == 'C': seq += 'G'
		elif c == 'G': seq += 'C'
		elif c == 'T': seq += 'A'
		else: seq += 'N'
	return seq
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

	
#!/usr/bin/env python3
import re
import sys
#making dictionary of multifasta sequences that keeps track of nucleotide compositions
#how to parse? Make a list of gene names and a list of sequences, and then make dictionary to link together
geneNames = []
geneSeq = []
seq = ""
seqs = {}
with open(sys.argv[1], "r") as file_contents:
	for line in file_contents:
		header = re.findall(r">(\w+)\s",line)	
		if header == []:
			cln_line = line.rstrip('\n')
			seq += cln_line
		else:
			geneNames.append(header[0])
			geneSeq.append(seq)
			seq = ''
#at the end, need to add that last sequence since don't have a header
	geneSeq.append(seq)		
	geneSeq = geneSeq[1:]
	print (geneNames, len(geneNames))
#	print (geneSeq, len(geneSeq))
	print (geneNames[1], type (geneNames[1]))
#now make a dictionary by iterating over each gene sequence, counting nucleotides, inserting into dict entry
	for i in range (len(geneSeq)):
#make first layer of dictionary - nucleotides and count for each individual gene		
		a_content = geneSeq[i].count("A")
		t_content = geneSeq[i].count("T")
		g_content = geneSeq[i].count("G")
		c_content = geneSeq[i].count("C")
#add nucleotide:counts dictionary to each gene		
		seqs[geneNames[i]] = {'A': a_content, 'T': t_content, 'G': g_content, 'C': c_content}

	for i in range (len(geneSeq)):
		print (geneNames[i] + '\t' + str(seqs[geneNames[i]]["A"])+ '\t'+ str(seqs[geneNames[i]]["T"])+'\t'+ str(seqs[geneNames[i]]['G']) + '\t' + str(seqs[geneNames[i]]['C']))


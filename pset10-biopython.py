#!/usr/bin/env python3
from Bio import SeqIO
import sys

#creates function that takes in fastafilename from cmd line and returns desired parameters
def fastaParser (filename):
	totSequences = 0
	totNucleotides = 0
	seq_length = []
	gc_content = []
	for seq_record in SeqIO.parse(filename, "fasta"):
		upper_seq = str(seq_record.seq).upper()
		seq_length.append(len(upper_seq))
		g_content = upper_seq.count("G")
		c_content = upper_seq.count("C")
		gc_content.append((g_content + c_content)/len(seq_record.seq))
		print ("Sequence name:", seq_record.name)
		print ("Sequence description:", seq_record.description)
		print ("Sequence:", seq_record.seq)
		totSequences += 1
		totNucleotides += len(seq_record.seq)
	print ("Total number of sequences:", totSequences)
	print ("Total number of nucleotides:", totNucleotides)
	print ("Average length of sequences:", totNucleotides/totSequences)
	print ("Shortest seq length:", min(seq_length))
	print ("Longest seq length:", max(seq_length))
	print ("Average GC content:", sum(gc_content)/totSequences)
	print ("Highest GC content:", max(gc_content))
	print ("Lowest GC content:", min(gc_content))

fastaParser(sys.argv[1])


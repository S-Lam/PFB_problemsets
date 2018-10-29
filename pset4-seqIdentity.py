#!/usr/bin/env python3
import sys
#Goal is to calculate sequence identity between two sequences. Only works for two strings. In this case, using a given fasta file
#first need to clean up input fasta file into separate strings for each sequence and excluding the header

header = []
sequence = []
seq = ''

#just to differentiate the first line from all other lines
firstline = True

with open (sys.argv[1], "r") as file_object:
	for line in file_object:
#only want lines that are not headers
		if ">" in line and firstline == True:
			string = line.rstrip("\n")
			header.append(string)
			firstline == False
		elif ">" in line and firstline == False:
			print (firstline)
			sequence.append(seq)
			string = line.rstrip("\n")
			header.append(string)
			seq = ''

		else:
			string = line.rstrip("\n")
			seq = seq + string
print (header)
print (sequence)
			



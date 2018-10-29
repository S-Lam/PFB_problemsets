#!/usr/bin/env python3
import sys
import re

#input with a fasta file (can be multiple) and parse to create dict of {gene1: {descrip: "", seq: ""}}
with open(sys.argv[1], "r") as file_object:
	header = []
	geneSeq = ''
	fastaDict = {}
	for line in file_object:
		header = re.findall(r">([\w\|\S]+)\s([\w\.\, ]+[^\n])", line)
		if header != []:
			if geneSeq != '': 
				fastaDict[geneName[0][0]] = {"desc":geneName[0][1], "seq": geneSeq}
				geneSeq = ''
				geneName = header 
			else:
				geneName = header
		else:
			cln_line = line.rstrip('\n')
			geneSeq += cln_line
	
	fastaDict[geneName[0][0]] = {"desc":geneName[0][1], "seq": geneSeq}
	for item in fastaDict:
		print ("Gene ID: {}\tDescription: {}\tSequence: {}".format(item, fastaDict[item]["desc"], fastaDict[item]["seq"]))
#	print (fastaDict)


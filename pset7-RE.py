#!/usr/bin/env python3
import sys
import re

#input with a fasta file (can be multiple) and parse to create dict of {gene1: {descrip: "", seq: ""}}
with open(sys.argv[1], "r") as file_object:
	header = []
	geneSeq = ''
	fastaDict = {}
	for line in file_object:
		header = re.findall(r">(.+[^\n])", line)
		print (header)
		if header != []:
			if geneSeq != '': 
				fastaDict[geneName[0]] = geneSeq
				geneSeq = ''
				geneName = header 
			else:
				geneName = header
		else:
			cln_line = line.rstrip('\n')
			geneSeq += cln_line
	
	fastaDict[geneName[0]] = geneSeq
#finding RE sites for each gene sequence
	for item in fastaDict:
	#	print ("Gene ID: {}\tDescription: {}\tSequence: {}".format(item, fastaDict[item]["desc"], fastaDict[item]["seq"]))
		sequence = fastaDict[item]
	# find restriction enzyme sites
		RE_list = re.findall(r"[AG]AATT[CT]",sequence)
		print ("Gene ID: {}\tRestriction Sites:{}".format(item, RE_list))
		cut_seq = re.sub(r"([AG])(AATT[CT])", r"\1^\2", sequence)
		print ("Gene ID: {}\tCut Sites in Sequence:{}".format(item, cut_seq))
	#determine lengths of fragments and sort in same order as they would separate on electrophoresis gel
		dig_seqlist = cut_seq.split("^")
		dig_seqlist.sort(key=len) # <- sorts the fragments based on length
		print ("Digested DNA fragments of increasing length: " , dig_seqlist)	

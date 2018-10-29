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

#making dictionary of restriction enzymes
re_dict = {}
with open("BioNet-noheader.txt","r") as file_object:
	for line in file_object:
#                       new_line = line.rstrip('\n')
                re_list = re.findall(r"(\w+)\s[(]*([\w\.]+)*[)]*\s+([\w\^\(\)]+)\n",line)
                if len(re_list) > 0:
                        re_tuple = re_list[0]
                        listlength = len(re_tuple)
                        if re_tuple[0] in re_dict:
                                re_dict[re_tuple[0]].append(re_tuple[listlength-1])
                                if re_tuple[1] != '':
                                        if re_tuple[1] in re_dict:
                                                re_dict[re_tuple[1]].append(re_tuple[listlength-1])
                                        else:
                                                re_dict[re_tuple[1]] = [re_tuple[listlength-1]]
                        else:
                                re_dict[re_tuple[0]] = [re_tuple[listlength-1]]
                                if re_tuple[1] != '':
                                        if re_tuple[1] in re_dict:
                                                re_dict[re_tuple[1]].append(re_tuple[listlength-1])
                                        else:
                                                re_dict[re_tuple[1]] = [re_tuple[listlength-1]]
#make dictionary not redundant, now key is enzyme and value is set of digestion sites
	for enzyme in re_dict:
        	re_dict[enzyme] = set(re_dict[enzyme])
#	print (re_dict)

#get digestion sites for restriction enzyme
	re_sites = re_dict[sys.argv[2]]
	cut_pattern = [] #make a list to store all the patterns that actually have cut sites with "^" because some don't grr
	for site in re_sites:
		if "^" in site:
			cut_pattern.append(site)
#now replace ambiguous IUPAC codes with regex patterns, will need list with "^" and without "^"
	regex_cutpatterns = []
	regex_nocutsite = []
	for pattern in cut_pattern:
		replaceR = re.sub(r'R', "[AG]",pattern)
		replaceRY = re.sub(r'Y', "[CT]", replaceR)
		replaceRYS = re.sub(r'S', "[GC]", replaceRY)
		replaceRYSW = re.sub(r'W', "[AT]", replaceRYS)
		replaceRYSWK = re.sub(r'K', "[GT]", replaceRYSW)
		replaceRYSWKM = re.sub(r'M', "[AC]", replaceRYSWK)
		replaceRYSWKMB = re.sub(r'B', "[CGT]", replaceRYSWKM)
		replaceRYSWKMBD = re.sub(r'D', "[AGT]", replaceRYSWKMB)
		replaceRYSWKMBDH = re.sub(r'H', "[ACT]", replaceRYSWKMBD)
		replaceRYSWKMBDHV = re.sub(r'V', "[ACG]", replaceRYSWKMBDH)
		replaceall = re.sub(r'N', "[ATGC]", replaceRYSWKMBDHV)
		regex_cutpatterns.append(replaceall)
		regex_nocutsite.append(replaceall.replace("^",""))
#finding RE sites for each gene sequence
	for item in fastaDict:
	#	print ("Gene ID: {}\tDescription: {}\tSequence: {}".format(item, fastaDict[item]["desc"], fastaDict[item]["seq"]))
		sequence = fastaDict[item]
	# find restriction enzyme sites
		RE_list = []
		for i in range(len(regex_nocutsite)):
			RE_list += (re.findall(regex_nocutsite[i],sequence)) #generating found cutsites in DNA
			cut_seq = re.sub(regex_nocutsite[i],regex_cutpatterns[i],sequence) #replacing sites with cutsites
		print (RE_list)
		print ("Gene ID: {}\tRestriction Sites:{}".format(item, RE_list))
		print ("Gene ID: {}\tCut Sites in Sequence:{}".format(item, cut_seq))
	#determine lengths of fragments and sort in same order as they would separate on electrophoresis gel
#		dig_seqlist = cut_seq.split("^")
#		dig_seqlist.sort(key=len) # <- sorts the fragments based on length
#		print ("Digested DNA fragments of increasing length: " , dig_seqlist)

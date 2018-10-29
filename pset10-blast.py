#!/usr/bin/env python3
from Bio import SeqIO
import re

filename = "../uniprot_sprot.fasta"
SpProteins = []
seqNum = 0
speciesList = []
for seq_record in SeqIO.parse(filename, "fasta"):
	seqNum += 1
	species = re.findall(r"OS=(\w+\s\w+\S]*)", seq_record.description)
	speciesList += species
	SpCheck = re.findall(r"Salmonella paratyphi B", seq_record.description) #checking specifically for salmonella paratyphi B
	if SpCheck != []:
		SpProteins.append(seq_record)	
print (speciesList)
print ("Total number of sequences:", seqNum)
speciesCount = {}
for species in speciesList:
	if species in speciesCount:
		speciesCount[species] += 1
	else:
		speciesCount[species] = 1
print (speciesCount)
#print (speciesCount["Salmonella paratyphi"])
#print (len(SpProteins))

#for writing salmonella paratyphi b proteins to fasta file
with open("s_paratyphi.prot.fa", "w") as file_object:
	SeqIO.write(SpProteins, file_object, "fasta")

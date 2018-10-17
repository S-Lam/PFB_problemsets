#! /usr/bin/env python3
DNA_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG','ATATATATCGAT','ATGGGCCC']
for item in DNA_list:
	print (item)

for item in DNA_list:
	print (len(item),"\t"+item)

#tuples

DNAtuples = [(len(item),item) for item in DNA_list]
for my_tuple in DNAtuples:
	print (str(DNAtuples.index(my_tuple)+1) + "\t" + str(my_tuple[0])+"\t" + my_tuple[1] + "\n")



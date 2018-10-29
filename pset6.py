#!/usr/bin/env python3

#opening Python_06.txt and uppercasing each line, printing out each line

new_file = open("Python_06_uc.txt","w")

with open("Python_06.txt", "r") as file_object:
	for line in file_object:
		line_upper = line.upper()
		new_file.write(line_upper)
	#	print (line_upper)
 		
new_file.close()

#opening and printing reverse complement of each Python_06_seq.txt

rev_comp_sequences = ""
with open("Python_06.seq.txt", "r") as file_object:

# first need to split each gene/sequence pair - new lines only count in computer language as \n no matter how long the actual seq is
	for line in file_object:
		identity, seq = line.split("\t")
		seq_clean = seq.rstrip("\n")
#replace the sequence with reverse complement
		replace_A = seq_clean.replace("A","t")
		replace_AT = replace_A.replace("T", "a")
		replace_ATG = replace_AT.replace("G", "c")
		replace_ATGC = replace_ATG.replace("C","g")
		complement = replace_ATGC.upper()
		rev_comp = complement[::-1]
		rev_comp_sequences += identity + "\t" + rev_comp + "\n"

print ("Reverse complement sequences from Python_06.seq.txt:\n" + rev_comp_sequences)

#count number of lines and number of characters per line of fastQ
with open ("Python_06.fastq", "r") as file_object:

#go through each line and keep track of each line and char, line ct == entries in char list
	charCt = []

# count number of characters per line
	for line in file_object:
		cleanline = line.rstrip("\n")
		charCt.append(len(cleanline))
	print ("Total number of lines:", len(charCt))
	print ("Total number of characters:", sum(charCt))
	print ("Average line length:", sum(charCt)/len(charCt), "characters per line")

#create sets of geneIDs of alpaca gene sets from Ensembl Biomart
allgenes = []
stemcellgenes = []
pigmentgenes = []
transFactors = []
#first make lists to format the individual geneIDs before adding to set
with open("alpaca_all_genes.tsv", "r") as file_object:
	for line in file_object:
		gene = line.rstrip("\n")	
		allgenes.append(gene)


with open("alpaca_stemcellproliferation_genes.tsv", "r") as file_object:
	for line in file_object:
		gene = line.rstrip("\n")	
		stemcellgenes.append(gene)



with open("alpaca_pigmentation_genes.tsv", "r") as file_object:
	for line in file_object:
		gene = line.rstrip("\n")	
		pigmentgenes.append(gene)

with open("alpaca_transcriptionFactors.tsv", "r") as file_object:
	for line in file_object:
		gene = line.rstrip("\n")	
		transFactors.append(gene)

#add gene lists to sets but exclude index 0 - the header
allgenes_set = set(allgenes[1:])

stemcellgenes_set = set(stemcellgenes[1:])

pigmentgenes_set = set(pigmentgenes[1:])

transFactors_set = set(transFactors[1:])

#find all the genes that are not stem cell proliferation genes
print ("The set of genes that are not stem cell proliferation genes:", allgenes_set - stemcellgenes_set)

#find all the genes that are both stem cell proliferation and pigmentation genes

print ("The set of genes that are both stem cell proliferation and pigmentation genes:", stemcellgenes_set & pigmentgenes_set)

print ("The set of genes that are transcription factors for stem cell proliferation:", stemcellgenes_set & transFactors_set)


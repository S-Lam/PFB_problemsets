#!/usr/bin/env python3
# calculate gc_content
def gc_content(dna):
	upperdna = dna.upper()
	g_content = dna.count("G")
	c_content = dna.count("C")
	gc_content = (g_content+c_content)/len(dna)
	percentage_gc = '{:.2%}'.format(gc_content)
#	print (gc_content)
	print("Percent GC content:",  str(percentage_gc))

#gives reverse complement of a dna sequence
def rev_complement(dna):
	upper_dna = dna.upper()
	a_replace = upper_dna.replace("A", "t")
	at_replace = a_replace.replace("T", "a")
	atg_replace =at_replace.replace("G", "c")
	atgc_replace =atg_replace.replace("C","g")
	compDNA = atgc_replace.upper()
	revCompDNA = compDNA[::-1]
	print( "Reverse Complement:", revCompDNA)

gc_content("CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA")

rev_complement("CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA")

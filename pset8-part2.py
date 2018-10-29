#!/usr/bin/env python3
import sys
import re
#function for generating reverse complement of sequence
def revComp (seq):
	seqUpper = seq.upper()
	replaceA = seqUpper.replace("A","t")
	replaceAT = replaceA.replace("T", "a")
	replaceATG = replaceAT.replace("G", "c")
	replaceATGC = replaceATG.replace("C", "g")
	rev_compSeq = replaceATGC.upper()[::-1]
	return rev_compSeq

def translate(seq,translation_table): #sequences are series of codons separated by spaces
	aaList = ''
	for codon in re.finditer(r'(\w{3})', seq):
		aaList += translation_table[codon.group(1)]
	return aaList

def maxPeptide (proteinSeq): #find the maximum peptide from list of aa's
	maxPeptide = ''
	for sequence in re.finditer(r'(M\w+)\*', proteinSeq):
		if len(sequence.group(1)) > len(maxPeptide):
			maxPeptide = sequence.group(1)
	return maxPeptide
	
#function for finding all the reading frames and writing to a file
def findreadingframes(gene,ntSeq, file_codons, file_aa):
	aa_file = open(file_aa, "a")
	maxpeptidefile = open("Python_08.translated-longest.aa","a")
	maxcodonfile = open("Python_08.orf-longest.nt", "a")
	maxProtSeq = ''
	maxcodonSeq = ''
	with open(file_codons, "a") as file_object:
		codons_fr1 = ''
		codons_fr2 = ''
		codons_fr3 = ''
#find frame1 codons
		print ("{}-frame1-codons".format(gene))	
		file_object.write(">{}-frame1-codons\n".format(gene))
		for codon in re.finditer(r'(\w{3})', ntSeq): #for first reading frame
			codons_fr1 += codon.group(1) + ' '
		print (codons_fr1)
		file_object.write(codons_fr1 +'\n')
		print ("{}-frame1-translated".format(gene)) #now translate the frame
		aa_file.write(">{}-frame1-translated\n".format(gene))
		aa_seq = translate(codons_fr1, translation_table)
		print (aa_seq)
		aa_file.write(aa_seq+'\n')
		peptide = maxPeptide(aa_seq)
		if len(peptide) > len(maxProtSeq):
			maxProtSeq = peptide
			maxcodonSeq = codons_fr1
#find frame2 codons
		print ("{}-frame2-codons".format(gene))	
		file_object.write(">{}-frame2-codons\n".format(gene))
		for codon in re.finditer(r'(\w{3})', ntSeq[1:]): #for second reading frame
			codons_fr2 += codon.group(1) + ' '
		print (codons_fr2)
		file_object.write(codons_fr2 +'\n')
		print ("{}-frame2-translated".format(gene)) #now translate the frame
		aa_file.write(">{}-frame2-translated\n".format(gene))
		aa_seq = translate(codons_fr2, translation_table)
		print (aa_seq)
		aa_file.write(aa_seq+'\n')
		peptide = maxPeptide(aa_seq)
		if len(peptide) > len(maxProtSeq):
			maxProtSeq = peptide
			maxcodonSeq = codons_fr2

#find frame3 codons
		print ("{}-frame3-codons".format(gene))	
		file_object.write(">{}-frame3-codons\n".format(gene))
		for codon in re.finditer(r'(\w{3})', ntSeq[2:]): #for third reading frame
			codons_fr3 += codon.group(1) + ' '
		print (codons_fr3)
		file_object.write(codons_fr3 +'\n')
		print ("{}-frame3-translated".format(gene)) #now translate the frame
		aa_file.write(">{}-frame3-translated\n".format(gene))
		aa_seq = translate(codons_fr3, translation_table)
		print (aa_seq)
		aa_file.write(aa_seq+'\n')
		peptide = maxPeptide(aa_seq)
		if len(peptide) > len(maxProtSeq):
			maxProtSeq = peptide
			maxcodonSeq = codons_fr3
#repeat for reverse complement:	
		rev_comp = revComp(ntSeq)
		codons_fr1 = ''
		codons_fr2 = ''
		codons_fr3 = ''
#find frame1 codons
		print ("{}-RevComp-frame1-codons".format(gene))	
		file_object.write(">{}-RevComp-frame1-codons\n".format(gene))
		for codon in re.finditer(r'(\w{3})', rev_comp): #for first reading frame
			codons_fr1 += codon.group(1) + ' '
		print (codons_fr1)
		file_object.write(codons_fr1 +'\n')
		print ("{}-RevComp-frame1-translated".format(gene)) #now translate the frame
		aa_file.write(">{}-RevComp-frame1-translated\n".format(gene))
		aa_seq = translate(codons_fr1, translation_table)
		print (aa_seq)
		aa_file.write(aa_seq+'\n')
		peptide = maxPeptide(aa_seq)
		if len(peptide) > len(maxProtSeq):
			maxProtSeq = peptide
			maxcodonSeq = codons_fr1
#find frame2 codons
		print ("{}-RevComp-frame2-codons".format(gene))	
		file_object.write(">{}-RevComp-frame2-codons\n".format(gene))
		for codon in re.finditer(r'(\w{3})', rev_comp[1:]): #for second reading frame
			codons_fr2 += codon.group(1) + ' '
		print (codons_fr2)
		file_object.write(codons_fr2 +'\n')
		print ("{}-RevComp-frame2-translated".format(gene)) #now translate the frame
		aa_file.write(">{}-RevComp-frame2-translated\n".format(gene))
		aa_seq = translate(codons_fr2, translation_table)
		print (aa_seq)
		aa_file.write(aa_seq+'\n')
		peptide = maxPeptide(aa_seq)
		if len(peptide) > len(maxProtSeq):
			maxProtSeq = peptide
			maxcodonSeq = codons_fr2
#find frame3 codons
		print ("{}-RevComp-frame3-codons".format(gene))	
		file_object.write(">{}-RevComp-frame3-codons\n".format(gene))
		for codon in re.finditer(r'(\w{3})', rev_comp[2:]): #for third reading frame
			codons_fr3 += codon.group(1) + ' '
		print (codons_fr3)
		file_object.write(codons_fr3 +'\n')
		print ("{}-RevComp-frame3-translated".format(gene)) #now translate the frame
		aa_file.write(">{}-RevComp-frame3-translated\n".format(gene))
		aa_seq = translate(codons_fr3, translation_table)
		print (aa_seq)
		aa_file.write(aa_seq+'\n')
		peptide = maxPeptide(aa_seq)
		if len(peptide) > len(maxProtSeq):
			maxProtSeq = peptide
			maxcodonSeq = codons_fr3
	maxpeptidefile.write('>{}-MaxPeptide\n{}\n'.format(gene, maxProtSeq))
	maxcodonfile.write('>{}-LongestORF\n{}\n'.format(gene, maxcodonSeq))
	maxpeptidefile.close()
	maxcodonfile.close()

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}
with open(sys.argv[1], "r") as file_contents:
#fasta parser
	fastaDict = {}
	geneName = ''
	seq = ''
	for line in file_contents:
		newline = line.rstrip("\n")
		if newline.startswith(">"):
			if seq == '':
				geneName = re.findall(r'>(\w+)\s',newline)[0]
			else:
				fastaDict[geneName] = seq
				geneName = re.findall(r'>(\w+)\s',newline)[0]
				seq = ''
		else:
			seq += newline
	fastaDict[geneName] = seq
#for each sequence, print codons from first reading frame
with open("Python_08.codons-frame1.nt", "w") as file_object:
	codons_fr1 = ''
	for gene in fastaDict:
#		print ("{}-frame1-codons".format(gene))	
		file_object.write("{}-frame1-codons\n".format(gene))
		for codon in re.finditer(r'(\w{3})', fastaDict[gene]): #for first reading frame
			codons_fr1 += codon.group(1) + ' '
#		print (codons_fr1)
		file_object.write(codons_fr1 +'\n')

#with open("Python_08.translated.aa", "w") as file_object:
	#codonReadingFrameList = []
codonfile = open('Python_08.codons-6frames.nt','w')
aafile = open('Python_08.translated.aa','w')
for gene in fastaDict:
#		findreadingframes(gene, fastaDict[gene], 'Python_08.codons-3frames.nt')
	#	codonReadingFrameList += findreadingframes(gene, fastaDict[gene], 'Python_08.codons-6frames.nt')
	#	print (codonReadingFrameList)
		
	findreadingframes(gene, fastaDict[gene], 'Python_08.codons-6frames.nt', 'Python_08.translated.aa')	
	#for sequence in codonReadingFrameList:
	#	aaSeq = translate(sequence, translation_table)
	#	print (aaSeq)
codonfile.close()
aafile.close()
		

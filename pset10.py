#!usr/bin/env python3

class DNASeq(object):
	def __init__(self, sequence, gene_name, organism):
		#adding attributes
		self.sequence = sequence
		self.gene_name = gene_name
		self.organism = organism
	
	def seq_length(self):
		return len(self.sequence)
	
	def nt_comp(self):
		upperSeq = self.sequence.upper()
		nt_A = upperSeq.count("A")
		nt_T = upperSeq.count("T")
		nt_G = upperSeq.count("G")
		nt_C = upperSeq.count("C")
		return {"A":nt_A, "T":nt_T, "G":nt_G, "C":nt_C}

	def gc_content(self):
		nt_count = self.nt_comp()
		numGC = nt_count["G"] + nt_count["C"]
		total_nt = numGC + nt_count["A"] + nt_count["T"]
		return numGC/total_nt

	def fasta_formatter(self):
		return ">{}\n{}\n".format(self.gene_name, self.sequence)
	

def compareDNAseq(dnaseq1, dnaseq2):
	if dnaseq1.sequence == dnaseq2.sequence and dnaseq1.gene_name == dnaseq2.gene_name and dnaseq1.organism == dnaseq2.organism:
		return True
	else:
		return False		
#create object
gene1 = DNASeq("ATGC", "gene_1", "unicorn")

#use object attributes to retrive and print them
print (gene1.sequence)
print (gene1.gene_name)
print (gene1.organism)

#use method to get sequence length
print(gene1.seq_length())

#use method to get nt composition
print (gene1.nt_comp())

#use method to get GC content
print("{:.1%}".format(gene1.gc_content()))

#use method to get FASTAfromatter
print (gene1.fasta_formatter())

#compare sequences

gene2 = DNASeq("ATGC", "gene_1", "unicorn")

gene3 = DNASeq("ATGC", "gene_2", "unicorn")
gene4 = DNASeq("ATGC", "gene_1", "dragon")
gene5 = DNASeq("ATC", "gene_1", "unicorn")

print (compareDNAseq(gene1, gene2))
print (compareDNAseq(gene1, gene3))
print (compareDNAseq(gene1, gene4))
print (compareDNAseq(gene1, gene5))

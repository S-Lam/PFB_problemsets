#!/usr/bin/env python3

#creating a shuffled sequence

import random
import sys

#get sequence as input
sequence = sys.argv[1]

#need to convert sequence to list to make it mutable
seq_list = list(sequence)
#randomize the sequence
for num in range(len(sequence)):
#choose two random positions within given sequence
	randPos1 = random.randrange(len(sequence))
	randPos2 = random.randrange(len(sequence))
	print (randPos1, randPos2)
#need to account for drawing the same base twice
	while randPos1 == randPos2:
		randPos1 = random.randrange(len(sequence))
		randPos2 = random.randrange(len(sequence))
		print ("second draw", randPos1, randPos2)
#for each random position, find corresponding nucleotide indexed there in sequence	
		base1 = seq_list[randPos1]
		base2 = seq_list[randPos2]
		print (base1, base2)
	else:
		base1 = seq_list[randPos1]
		base2 = seq_list[randPos2]
		print (base1, base2)
	
#now swap bases with random positions chosen
	seq_list[randPos1] = base2
	seq_list[randPos2] = base1
	print (seq_list)
#join list to make a string at the end
scr_seq = "".join(seq_list)
print (scr_seq)

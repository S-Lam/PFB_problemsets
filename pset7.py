#!/USr/bin/env python3
import re

#find every occurence of "nobody"
count = 0
#relative to line
with open("Python_07_nobody.txt", "r") as file_object:
	for line in file_object:
		updated_line = line.rstrip("\n")
		for match in re.finditer("Nobody", updated_line):
			print ("Start position of 'Nobody'relative to start of line", match.start() + 1)
			count += 1
	print ("Total occurrences of 'Nobody':", count)
#position relative to entire string including \n's
with open("Python_07_nobody.txt", "r") as file_object:
	contents = file_object.read()
	for match in re.finditer("Nobody", contents):
		print ("Start position of 'Nobody':", match.start() + 1)

#replace "Nobody" with "Gerald"
with open("Python_07_nobody.txt", "r") as file_object:
	contents = file_object.read()
	Gerald_sub = re.sub("Nobody", "Gerald", contents)
	print (Gerald_sub)

#find all the header lines in Python_07.fasta
with open("Python_07.fasta", "r") as file_object:
	contents = file_object.read()
	found = re.findall(r">.+[^\n]", contents)
	print ("Headers:",found)

#now extract the sequence name and description using subpatterns
with open("Python_07.fasta", "r") as file_object:
	contents = file_object.read()
	for (geneName, descrip) in re.findall(r">([\w\|\.]+)\s([^\n]+)", contents):
		print("GeneID:", geneName+ "\n"+"Description:", descrip)


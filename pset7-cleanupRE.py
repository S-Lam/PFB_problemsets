#!/usr/bin/env python3
import sys
import re
re_dict = {}
#with open("bionet.txt","r") as file_object:
#only want data, not the header to this file
#	Data = False	
	#cleanfile = open("BioNet-noheader.txt","w")
#	for line in file_object:
#		if Data == True:
		#	cleanfile.write(line)
	#	elif "AaaI" in line:
		#	cleanfile.write(line)
	#		Data = True
	#cleanfile.close()
	#print ("File written") 
#make dictionary of enzymes and cutting sites
with open("BioNet-noheader.txt","r") as file_object:
	for line in file_object:
#			new_line = line.rstrip('\n')
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
#make dictionary not redundant
	for enzyme in re_dict:
		re_dict[enzyme] = set(re_dict[enzyme])
	print (re_dict)


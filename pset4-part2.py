#!/usr/bin/env python3
import sys
for num in range(int(sys.argv[1]),int(sys.argv[2])+1):
	if num % 2 != 0:
		print (num)

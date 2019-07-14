#!/usr/bin/env python
import sys
import re

def isInt(text):
	try:
		int(text)
	except:
		return False
	return True

i = 0


for line in sys.stdin:

	cols = line.split(',')
	severity = cols[4]
	weather = cols[8]
	age = cols[17]
	
	if isInt(severity) and isInt(weather) and isInt(age):
		if int(severity) == 1 and int(weather) == 1 and int(age) < 50:
			print cols[0], 1
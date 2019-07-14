#!/usr/bin/env python
import sys
import string

def removePunctuation(sentence):
	#Python 3:
	# table = str.maketrans({key: None for key in string.punctuation})
	# return sentence.translate(table).lower()

	#Python 2:
	table = string.maketrans("","")
	return sentence.translate(None, string.punctuation).lower()



for line in sys.stdin:
	line = removePunctuation(line)
	words = line.strip().split()
	for word in words:
		print (word)

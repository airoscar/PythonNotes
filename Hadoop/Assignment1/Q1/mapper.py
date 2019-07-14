#!/usr/bin/env python
import sys
import re

def convertToListOfWords(sentence):
	sentence = sentence.lower()
	words = re.split('\W', sentence)
	words = [word for word in words if len(word)>0]
	return words


for line in sys.stdin:
	words = convertToListOfWords(line)
	bigrams = zip(words, words[1:])
	
	for gram in bigrams:
		print gram, "=>>1"


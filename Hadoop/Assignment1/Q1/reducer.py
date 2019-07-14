#!/usr/bin/env python

import sys

bigramsCount = {}

for line in sys.stdin:
	line = line.strip()
	bigram, count = line.split("=>>")

	count = int(count)

	if bigram in bigramsCount:
		bigramsCount[bigram] += count
	else: 
		bigramsCount[bigram] = count

for bigram in bigramsCount:
	print bigram, bigramsCount[bigram]
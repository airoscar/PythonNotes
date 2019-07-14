#!/usr/bin/env python

import sys

total=0
yearDict = dict()

for line in sys.stdin:
	contents = line.strip().split()
	year = contents[0]
	count = int(contents[1])
	if year in yearDict:
		yearDict[year] += count
	else:
		yearDict[year] = count

for key in yearDict:
	print key, yearDict[key]

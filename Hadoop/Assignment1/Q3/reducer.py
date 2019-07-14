#!/usr/bin/env python
import sys

words = set()

for line in sys.stdin:
	words.add(line.strip())

sortedWords = sorted(words)

for word in sortedWords:
	print word
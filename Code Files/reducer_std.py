#!/usr/bin/env python
import sys
 
# maps words to their counts
word2count = {}

total_no_of_years = 0
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = float(count)
    except ValueError:
        continue

    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count
    
    if(word == "***"):
        total_no_of_years += 1
 
# write the tuples to stdout
# Note: they are unsorted
for word in word2count.keys():
    print '%s\t%s'% (word, ((float(word2count[word])-float(word2count[word]/total_no_of_years))**2)/len(word2count))
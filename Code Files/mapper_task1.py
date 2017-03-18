#!/usr/bin/env python
import sys
import string
import re
 
#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- remove the punctuation
    lines_p=re.sub('[^*a-z\s]',' ',line)

    #---remove all the HTML tags -- I did not have any HTML tags in my document but regardless I included the script to remove them.
    #lines_f = re.sub(“<.*?>”,” ”,lines_p)

    #--- split the line into words ---
    words = lines_p.split()

    #--- output tuples [word, 1] in tab-delimited format---
    for word in words:
        print '%s\t%s' % (word, "1")
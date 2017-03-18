# Contextual-Analysis-of-Presidential-Speeches

Task 1: Specific Word counts:

INPUT:	The	data	files	in	incremental	size	order.
OUTPUT:	The	specific	word	counts	for	each	file	(Attached	-Sample	output- Task	1.txt)
The	reducer.py	was	kept	unchanged	for	this	task.	The	sample	output	file	is	attached	in	
the	zip	file	of	this	submission.




TASK	2:
Calculating	the	Average	use	of	every	word	(all	Addresses):
Modify	the	reducer	to	divide	the	count	of	each	word	to the	no	of	
years	to	obtain	the	average	of	each	word	per	year	(for	all	the	addresses)

The	average	of	every	word	is	computed	from	1790-2016.	See results in output file.


Computing	Standard	Deviation:

Included	the	computation	of	for	the	standard	deviation	:
word,	((float(word2count[word])- float(word2count[word]/total_no_of_years))**2)/len(word2count))

This	line	would	calculate	the	average	by	dividing	the	count	of	every	word	with	the	total	
number	of	years	and	taking a	square	it	and	then	dividing	the	whole	value	obtained	with	
the	total	no	of	words	in	the	document.	This	is	the	same	as	the	standard	deviation	
formula.

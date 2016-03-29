
# remove lines containing (TV), (VG) and {} from ratings 

#!/usr/bin/python
import sys

if len(sys.argv) < 3:
    sys.exit("Usage: filter.py input output")

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')

print "Please wait, it may take few seconds..."

lines = inputFile.readlines()

for line in lines:
	if '{' not in line: 
		outputFile.write(line)


outputFile.close()
inputFile.close()
		
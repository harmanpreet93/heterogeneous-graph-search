#!/usr/bin/python
import sys

if len(sys.argv) < 3:
    sys.exit("Usage: pythonFile input output")

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')

print "processing..."

lines = inputFile.readlines()

count = 0
for line in lines:
	outputLine = ''
	arr = line.split(',')
	try:
		if int(arr[3]) > 100:
			outputFile.write(line)
	except Exception, e:
		pass
	
outputFile.close()
inputFile.close()
		
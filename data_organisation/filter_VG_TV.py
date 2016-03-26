#!/usr/bin/python
import sys

if len(sys.argv) < 3:
    sys.exit("Usage: python_file input output")

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')

print "Please wait, it may take few seconds..."

lines = inputFile.readlines()

for line in lines:
	# arr = line.split(''
	if '(TV)' not in line and '(VG)' not in line:
		outputFile.write(line)

outputFile.close()
inputFile.close()
		
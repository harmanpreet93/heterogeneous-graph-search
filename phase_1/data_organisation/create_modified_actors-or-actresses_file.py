#!usr/bin/python
import sys
import re

'''
Create modified actors file from actresses.txt with syntax as follow:
Eg: actor,<movies actor acted in>
'''

def createHashmap(inputFile,outputFile):
	actorsHashmap = []
	print "Please wait, it may take few seconds..."
	lines = inputFile.readlines()

	for line in lines:
		arr = line.split(',')
		actor = arr[1].lstrip().rstrip() + ','
		movies = ''
		movies += arr[2][2:-1].lstrip().rstrip() + ','
		for x in range(3,len(arr)-1):
			movies += arr[x][2:-1].lstrip().rstrip() + ','
		last_movie = arr[-1][2:-3].lstrip().rstrip() + '\n'
		movies += last_movie
		# print actor+movies
		outputFile.write(actor+movies)

	inputFile.close()
	outputFile.close()

def write_in_outputFile(actorsHashmap,outputFile):
	outputFile.write(actorsHashmap)
	outputFile.close()

if __name__ == '__main__':

	if len(sys.argv) < 3:
		sys.exit("Usage: python fileName.py actors.txt modified_actors.txt")

	actorsFile = open(sys.argv[1],'r')
	outputFile = open(sys.argv[2],'w')	

	actorsHashmap = createHashmap(actorsFile,outputFile)








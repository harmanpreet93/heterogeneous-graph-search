#!usr/bin/python
import sys
import re

def createHashmap(inputFile):
	actorsHashmap = {}
	print "Please wait, it may take few seconds..."
	lines = inputFile.readlines()

	for line in lines:
		arr = line.split(',')
		actor = arr[0].lstrip().rstrip() + ' ' + arr[1].lstrip().rstrip()
		if actorsHashmap.has_key(actor):
			actorsHashmap[actor].append(arr[2].lstrip().rstrip())
		else:
			movie = list()
			movie.append(arr[2].lstrip().rstrip())
			actorsHashmap[actor] = movie

	inputFile.close()
	return actorsHashmap

def createStats(actorsHashmap,outputFile):

	for key in actorsHashmap:
		if(len(actorsHashmap[key]) == 1):
			values = re.split("\(|\)|\/",actorsHashmap[key][0])
			year = values[len(values)-2]
			try:
				if(int(year)>2010):
					line = ""
					line += str(len(actorsHashmap[key])) + ","
					line += key + ","
					line += str(actorsHashmap[key]) + '\n'
					outputFile.write(line)

			except ValueError:
				if(int(values[len(values)-3])>2010):
					line = ""
					line += str(len(actorsHashmap[key])) + ","
					line += key + ","
					line += str(actorsHashmap[key]) + '\n'
					outputFile.write(line)
					print 'year: ', values[len(values)-3]
		elif (len(actorsHashmap[key]) > 1):
			line = ""
			line += str(len(actorsHashmap[key])) + ","
			line += key + ","
			line += str(actorsHashmap[key]) + '\n'
			outputFile.write(line)

	outputFile.close()


if __name__ == '__main__':

	if len(sys.argv) < 3:
		sys.exit("Usage: python fileName.py actresses.csv outputFile")

	actressesFile = open(sys.argv[1],'r')
	outputFile = open(sys.argv[2],'w')	

	actorsHashmap = createHashmap(actressesFile)
	print len(actorsHashmap)
	createStats(actorsHashmap,outputFile)








#!usr/bin/python
import sys

def findDistinctMovies(inputFile):
	movieHashmap = {}
	print "Please wait, it may take few seconds..."
	lines = inputFile.readlines()

	for line in lines:
		arr = line.split(',')
		movie = arr[2].lstrip().rstrip()
		if not(movieHashmap.has_key(movie)):
			movieHashmap[movie] = movie
			# outputFile.write(movie + '\n')

	inputFile.close()
	# outputFile.close()
	return movieHashmap

if __name__ == '__main__':

	if len(sys.argv) < 3:
		sys.exit("Usage: python fileName.py actors.csv actresses.csv")

	actorsFile = open(sys.argv[1],'r')
	actressesFile = open(sys.argv[2],'r')

	actorsHashMap = findDistinctMovies(actorsFile)
	actressesHashMap = findDistinctMovies(actressesFile)

	movies = actorsHashMap.copy()
	movies.update(actressesHashMap)

	print len(movies)










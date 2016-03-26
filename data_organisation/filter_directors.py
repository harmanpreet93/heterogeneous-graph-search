#!usr/bin/python
import sys

def createMoviesHashmap(inputFile):
	moviesHashmap = {}
	print "Please wait, it may take few seconds..."
	lines = inputFile.readlines()

	for line in lines:
		arr = line.split(',')
		movie = arr[0].lstrip().rstrip()
		# if moviesHashmap.has_key(movie):
		# moviesHashmap[movie].append(arr[2].lstrip().rstrip())
		# else:
		# movie = list()
		# movie.append(arr[2].lstrip().rstrip())
		moviesHashmap[movie] = movie

	inputFile.close()
	return moviesHashmap

def createDirectorsOutputFile(directorsFile,moviesHashmap,outputFile):

	lines = directorsFile.readlines()

	for line in lines:
		arr = line.split(',')
		movie = arr[2].lstrip().rstrip()

		if moviesHashmap.has_key(movie):
			outputFile.write(line)

	# for key in moviesHashmap:
	# 	line = ""
	# 	line += str(len(moviesHashmap[key])) + ","
	# 	line += key + ","
	# 	line += str(moviesHashmap[key]) + '\n'
	# 	outputFile.write(line)

	outputFile.close()


if __name__ == '__main__':

	if len(sys.argv) < 4:
		sys.exit("Usage: python fileName.py movies.csv directors.csv outputFile")

	actorsFile = open(sys.argv[1],'r')
	directorsFile = open(sys.argv[2],'r')
	outputFile = open(sys.argv[3],'w')	

	moviesHashmap = createMoviesHashmap(actorsFile)
	# print len(moviesHashmap)
	createDirectorsOutputFile(directorsFile,moviesHashmap,outputFile)








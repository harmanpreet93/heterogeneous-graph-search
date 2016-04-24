#!usr/bin/python

from py2neo import authenticate,Graph
from py2neo import Node, Relationship
# from py2neo import watch
import sys

def connect_graph():
	# watch('httpstream')
	user_name = 'neo4j'
	password = 'neo4j123'
	
	# port for http: 7474 and for https: 7473
	host_port = 'localhost:7474'
	URI = 'localhost:7474/db/data'
	
	# set up authentication parameters
	authenticate(host_port,user_name,password)

	# connect to authenticated graph database
	graph = Graph("http://"+host_port+"/db/data/")
	print 'graph connected'
	return graph

# create genre node 
def create_genre_node(graph,label,genre_name):
	return graph.merge_one(label,'name',genre_name)

# create relationship movie-[GENRE]->genre
def create_movie_genre_relationship(graph,node,movie_name):
	for movie in graph.find('movie','title',movie_name):
		genre = Relationship(movie,"GENRE",node)
		graph.create_unique(genre)
		break

# creates genre node, then create relationships between genres and movies
def upload_genres_data(graph):
	if len(sys.argv) < 2:
		sys.exit("Usage: python file_name.py genre.csv")

	genre_file = open(sys.argv[1],'r')
	print "Please wait, it may take some time to create relationships..."
	genres = genre_file.read().splitlines()
	for line in genres:
		arr = line.split(',')
		node = create_genre_node(graph,'genre',arr[1])
		create_movie_genre_relationship(graph,node,arr[0])
		print arr[0]
		
	genre_file.close()

if __name__ == '__main__':
	graph = connect_graph()
	upload_genres_data(graph)



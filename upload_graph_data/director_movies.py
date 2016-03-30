#!usr/bin/python

'''
Data from modified_directors.csv is uploaded to nei4j using following steps:
	- For each director, create a node with label 'director' and property 'name'
	- For each director, find all the movies that the director has directed in and 
		create a relationship between the two

	Structure of modified_directors.txt file:
	- director,<movies director has directed>
	For eg: Alex Karpovsky,Red Flag (2012),Rubberneck (2012),The Hole Story (2005)
	  
'''

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

# create director node 
def create_director_node(graph,label,director_name):
	return graph.merge_one(label,'name',director_name)

def create_relationship(graph,node,movie_name):
	for movie in graph.find('movie','title',movie_name):
		directed = Relationship(node,"DIRECTED",movie)
		graph.create_unique(directed)
		break

# creates directors node, then create relationships between director and movies he directed
def upload_directors_data(graph):
	# directors_file = open(path/to/modified_directors.txt,'r') 
	if len(sys.argv) < 2:
		sys.exit("Usage: python fileName.py directors.csv")

	directors_file = open(sys.argv[1],'r')
	print "Please wait, it may take some time to create director nodes and its relationships with movies..."
	directors = directors_file.read().splitlines()

	for line in directors:
		arr = line.split(',')
		node = create_director_node(graph,'director',arr[0])
		for x in range(1,len(arr)):
			create_relationship(graph,node,arr[x])
	directors_file.close()

if __name__ == '__main__':
	graph = connect_graph()
	upload_directors_data(graph)



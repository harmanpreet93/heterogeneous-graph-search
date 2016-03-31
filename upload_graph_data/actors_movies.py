#!usr/bin/python

'''
Data from modified_actors.txt is uploaded to nei4j using following steps:
	- For each actor, create a node with label 'actor' and property 'name'
	- For each actor, find all the movies that the actor has acted in and 
		create a relationship between the two

	Structure of modified_actors.txt file:
	- actor,<movies actor acted in>
	  For eg: James (II) Coyne,Man-Thing (2005),'Missing Sock (2004)
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

# create actor node 
def create_actor_node(graph,label,actor_name):
	return graph.merge_one(label,'name',actor_name)

def create_relationship(graph,node,movie_name):
	for movie in graph.find('movie','title',movie_name):
		acted_in = Relationship(node,"ACTED_IN",movie)
		graph.create_unique(acted_in)
		break

# creates actors node, then create relationships between actors and movies he acted in
def upload_actors_data(graph):
	# actors_file = open(path/to/modified_actors.txt,'r') 
	if len(sys.argv) < 2:
		sys.exit("Usage: python file_name.py actors.csv")

	actors_file = open(sys.argv[1],'r')
	print "Please wait, it may take some time to create relationships..."
	actors = actors_file.read().splitlines()
	for line in actors:
		arr = line.split(',')
		node = create_actor_node(graph,'actor',arr[0])
		for x in range(1,len(arr)):	
			create_relationship(graph,node,arr[x])
	actors_file.close()

if __name__ == '__main__':
	graph = connect_graph()
	upload_actors_data(graph)



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
	# first check if node already exists
	for node in graph.find(label,'name',actor_name):
		for rel in graph.match(start_node=node,bidirectional=True):
			graph.delete(rel)
		graph.delete(node)
	
	node = Node(label,name=actor_name)
	# graph.create returns tuple of nodes 
	return graph.create(node)

# delete all nodes of particular label with no relationships
def delete_label(graph,label):
	print "deleting nodes with label ", label
	for node in graph.find(label):
		graph.delete(node)

# delete all relationships for particular type
def delete_relationships(graph,relationship_type):
	for rel in graph.match(rel_type=relationship_type):
		graph.delete(rel)

# delete selected nodes with no relationships attached 
def delete_selected_nodes(graph,label,property_key,property_value):
	for node in graph.find(label,property_key,property_value):
		graph.delete(node)

def create_relationship(graph,node,movie_name):
	for movie in graph.find('movie','title',movie_name):
		# print 'movie found in graph db: ',movie
		acted_in = Relationship(node,"ACTED_IN",movie)
		graph.create(acted_in)
		break

# creates actors node, then create relationships between actor and movies he acted in
def upload_actors_data(graph):
	# actors_file = open(path/to/modified_actors.txt,'r')
	actors_file = open(sys.argv[1],'r')
	print "Please wait, it may take some time..."
	actors = actors_file.read().splitlines()

	for line in actors:
		arr = line.split(',')
		node = create_actor_node(graph,'actor',arr[0])
		for x in range(1,len(arr)):
			create_relationship(graph,node[0],arr[x])

if __name__ == '__main__':
	graph = connect_graph()
	# delete_relationships(graph,"ACTED_IN")
	# delete_label(graph,'actor')
	upload_actors_data(graph)
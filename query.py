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
from py2neo.packages.httpstream import http 
# from py2neo import watch
import operator
import sys

def connect_graph():
	# watch('httpstream')
	user_name = 'neo4j'
	password = 'neo4j123'
	
	# port for http: 7474 and for https: 7473
	host_port = 'localhost:7474'
	URI = 'localhost:7474/db/data'
	http.socket_timeout = 9999
	
	# set up authentication parameters
	authenticate(host_port,user_name,password)

	# connect to authenticated graph database
	graph = Graph("http://"+host_port+"/db/data/")
	print 'graph connected'
	return graph

def execute_query(query):
	cypher = graph.cypher
	result = cypher.execute(query)
	return result

if __name__ == '__main__':

	actor_input = raw_input('Enter the actor for whom to find similarity: ')
	top_K = raw_input('Enter the actor for whom to find similarity: ')


	graph = connect_graph()
	query_xx = "MATCH (a:actor {name:'"+str(actor_input)+"'})-[ACTED_IN]->(m) MATCH (m)<-[r:ACTED_IN]-(a) RETURN a as actor,count(a.name) as count"
	xx = execute_query(query_xx)
	
	for result in xx:
		xx_value = int(result.count)
		break

	query_xy = "MATCH (a:actor {name:'"+str(actor_input)+"'})-[r1:ACTED_IN]->(m1:movie)<-[r2:ACTED_IN]-(b:actor) RETURN b as actor,count(b.name) as count"
	xy = execute_query(query_xy)

	hashmap = {}
	for result in xy:
		hashmap.setdefault(result.actor,[]) 
		hashmap[result.actor].append(result.count)

	query_yy = "MATCH (a:actor {name:'"+str(actor_input)+"'})-[r1:ACTED_IN]->(m1:movie)<-[r2:ACTED_IN]-(b:actor) MATCH (b)-[r3:ACTED_IN]->(m) MATCH (m)<-[r4:ACTED_IN]-(b) RETURN b as actor,count(b.name) as count"
	yy = execute_query(query_yy)

	for result in yy:
		hashmap[result.actor].append(result.count)

	# print hashmap

	for key in hashmap:
		xy_value = int(hashmap[key][0])
		yy_value = int(hashmap[key][1])
		score = 2 * xy_value / (xx_value+yy_value)
		hashmap[key].append(score)

	sorted_hashmap = sorted(hashmap.items(), key=lambda e: e[1][2])
	for key in sorted_hashmap:
		print key, sorted_hashmap[key][2]


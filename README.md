## Heterogeneous Graph Search

In this project we aim to implement searching in a heterogeneous graph network. To achieve this, the implementation was divided into two phases. Phase 1 includes data extraction and filtering, and organisation of data in a graph based database. Phase 2 includes defining weights for adjacent nodes and edges depending upon various attributes so as to find the nodes “nearest” to each other with respect to the distance metric defined in this regard.

## Note:
1. Always delete relationship first before deleting the nodes.

## Phase 1. Data Extraction, Filtering and Organisation:
Refer [Phase-1](https://github.com/harmanpreet93/heterogeneous-graph-search/tree/master/phase_1) for Data Extraction and Filtration.

## Graph Data Upload
After filtering the data and structuring it into CSV files, the data was entered into a graph database, so as to visualize the entities and their relationships. The [Neo4j](http://neo4j.com/) database was used for this purpose. Data was entered with the help of the [Cypher Query Language](http://neo4j.com/docs/stable/cypher-query-lang.html) and  the [Py2neo-2.0](http://py2neo.org/2.0/) client library in the following steps:     
  1. The *movies.csv* file was simply imported into the Neo4j database, creating a node per movie.
  2. To import actors into the database, py2neo scripts were written so as to check for each actor-movie pair, whether the node (the entity) for the actor already exists in the database. If so, the existing node for the actor was linked to the paired movie with the help of an edge (the relationship). Else, a new node was formed for the actor and a relationship was formed with the existing paired movie.
  3. Step-2 was repeated for *actresses*, *directors* and *movie-genres*.    

As a result of the above steps, we obtained a heterogeneous graph representation of the filtered data in the Neo4j database, complete with nodes representing the movies, actors, actresses, directors, and movie genres, and edges representing their corresponding relationships.

## Phase 2. Finding similar nodes
In the representation obtained in the Neo4j database, given a node in the heterogeneous graph, the objective of Phase 2 is to find the closest match for the node among the other nodes. For this, we aim to define a distance metric for two nodes of the same type, for which we will take various factors into consideration, and assign weights to each of the factors. Based on this metric, we will create a ranking of the other nodes, to represent the similarity measure. This measure will serve as the basis for finding similar nodes in the heterogeneous graph.
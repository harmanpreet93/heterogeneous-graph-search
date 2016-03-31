#### Import data in neo4j from CSV files
`LOAD CSV WITH HEADERS FROM 'file:///path_to_csv_file' AS line CREATE (:movie {title: line.title, year: line.year, rating: line.rating, votes: line.votes})`

#### Get node count for particular label
`MATCH (n:label) RETURN count(*) AS num_of_nodes`

#### Get count of total nodes
`MATCH (n) RETURN count(*) AS total_nodes`

#### Get the count of movies actors have acted in
`MATCH (a:actor)-[r:ACTED_IN]->(m:movie) RETURN a.name as Actor,count(r) AS num_of_movies_acted_in ORDER BY num_of_movies_acted_in DESC LIMIT 10`

### Get all the movies that an actor ACTED_IN
`MATCH (a:actor {name:'Brad Pitt'})-[r:ACTED_IN]->(m:movie) RETURN r`

#### Get all incoming nodes to the movie
`MATCH (m:movie {title:'A Good Year (2006)'})<-[r]-()RETURN r`

#### Get all the directors count for each movie in decreasing order of number of movies 
`MATCH (m:movie)<-[r:DIRECTED]-(d:director) RETURN m.title as movie,count(d) as directors_count ORDER BY directors_count DESC LIMIT 100`


Variable length relationships

Nodes that are a variable number of relationship→node hops away can be found using the following syntax: -[:TYPE*minHops..maxHops]->. minHops and maxHops are optional and default to 1 and infinity respectively. When no bounds are given the dots may be omitted.

MATCH (a:actor { name:'James Le Gros' })-[r:ACTED_IN*1..2]->() RETURN r,a

Finding a single shortest path between two nodes is as easy as using the shortestPath function.
MATCH (martin:Person { name:"Martin Sheen" }),(oliver:Person { name:"Oliver Stone" }),
  p = shortestPath((martin)-[*..15]-(oliver))
RETURN p

This means: find a single shortest path between two nodes, as long as the path is max 15 relationships long. Inside of the parentheses you define a single link of a path — the starting node, the connecting relationship and the end node. Characteristics describing the relationship like relationship type, max hops and direction are all used when finding the shortest path. You can also mark the path as optional.
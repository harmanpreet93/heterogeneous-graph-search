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
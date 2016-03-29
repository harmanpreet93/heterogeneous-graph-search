#### Import data in neo4j from CSV files
`LOAD CSV WITH HEADERS FROM 'file:///path_to_csv_file' AS line CREATE (:movie {title: line.title, year: line.year, rating: line.rating, votes: line.votes})`

#### Get node count for particular label
`MATCH (n:label) RETURN count(*)`

#### Get count of total nodes
`MATCH (n) RETURN count(*)`

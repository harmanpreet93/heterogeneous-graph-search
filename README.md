## Heterogeneous Graph Search

In this project we aim to implement searching in a heterogeneous graph network. To achieve this, the implementation was divided into two phases. Phase 1 includes data extraction and filtering, and organisation of data in a graph based database. Phase 2 includes defining weights for adjacent nodes and edges depending upon various attributes so as to find the nodes “nearest” to each other with respect to the distance metric defined in this regard.


## Phase 1. Data Extraction, Filtering and Organisation:

### A. Data Extraction

For this project, we used a subset of the IMDB database, which was provided for use at [http://ftp.fu-berlin.de/pub/misc/movies/database/](http://ftp.fu-berlin.de/pub/misc/movies/database/). The data was downloaded in the form of list files containing unstructured information about actors, directors, genres, movies. plots, cinematographers, etc. The list files for only actors, actresses, directors,  movies, movie-ratings, and genres were extracted, containing the following data format:

**Actors**:
*(Lastname, Firstname #TITLE <!(detail)/> <!(detail)/> <![role]/> <!<billingPosition>/>)*

**Actresses**:
*(Lastname, Firstname #TITLE <!(detail)/> <!(detail)/> <![role]/> <!<billingPosition>/>)*

**Directors**: 
*(Lastname, Firstname #TITLE <!(detail)/>)*

**Ratings**: 
*(Dist.Num Votes Rank #TITLE)*

**Movies**: 
*(#TITLE Year)*

**Genres**: 
*(#TITLE Genre)*

**_Legend_**:    
*<!xxx/>*: *optional*    
*#TITLE*: *name (year) <!(info)/> <!{<!episodeName/><!{episodeNum}/>}/> <!{{SUSPENDED}}/>*     

### B. Data Filtering
The next step was to structure and filter the data properly as per the requirements of the project. The list files were used to generate structured CSV files for each of the entities. Each CSV file was obtained after multiple levels of filters applied using python scripts. The filters applied, and the data statistics obtained after each step are described below.

#### 1. Converting list files to CSV files
The list files were iterated and useful information was extracted to structure the data into CSV files as follows:

  **Movies**: `(title,year,rating,votes)`     
  **Actors**: `(first_name,last_name,movie_title)`     
  **Actresses**: `(first_name,last_name,movie_title)`    
  **Directors**: `(first_name,last_name,movie_title)`    
  **Genres**: `(movie_title,genre)`    
  
  
#### 2. Loading csv files into database

#### Challenge faced:    
##### Large file sizes    
The output CSV files were very large in size and couldn’t be loaded into the Neo4j database using web interface. Each trial resulted in a database disconnection error because too much time went into loading these large files, leading to a timeout or memory error in most cases.    

##### Approach 1: Splitting the data
We tried to split the data into multiple small files, and tried to load each file individually. However, still the problem remained, and the size of file successfully loading into the database was too small.

##### Approach 2: Data Filtering using SQL
The data needed to be filtered in order to insert into the database so as to use it for phase 2. To collect the stats for the data and filter accordingly. We tried to load subsets of the data into a MySQL database. But again due to large file sizes, we failed to do so.

##### Approach 3: Manual Filtering
Finally, we decided to manually filter the data by deciding some factors and thresholds, and wrote scripts in Python to obtain the desired filtered data sets.    

**Code Description and Usage**:

A. Removal of movies without rating data: **tsv2csv.py**    
  Usage: `python tsv2csv.py input.csv output.csv`

B. Removal of TV series and video­games by removal of tags (TV), (VG), (V), {}: **filter_VG_TV.py,filter_V.py,filter_bracket.py**  
  Usage: `python filter_VG_TV.py input.csv output.csv`    
  Usage: `python filter_V.py input.csv output.csv`    
  Usage: `python filter_bracket.py input.csv output.csv`    

C. Removal of movies released before 2000: **filter_year_2000.py**    
  Usage: `python filter_year_2000.py input.csv output.csv`    

D. Removal of movies with number of votes < 100: **filter_number_of_votes.py**    
  Usage: `python filter_number_of_votes.py input.csv output.csv`   

E. Finding distinct #Actors and #Actresses for filtered movies: **distinct_actors.py, distinct_actresses.py**    
  Usage: `python distinct_actors.py actors.csv output.csv`    
  Usage: `python distinct_actresses.py actresses.csv output.csv`    

F. Removal of actors and actresses who acted in only one movie released before 2010: **distinct_actors_2010.py, distinct_actresses_2010.py**   
  Usage: `python distinct_actors_2010.py actors.csv output.csv`    
  Usage: `python distinct_actresses_2010.py actresses.csv output.csv`    

G. Removal of movies without any associated actors or actresses: **find_union_movies.py**    
  Usage:`'python find_union_movies.py actors.csv actresses.csv`    

H. Filtering of directors for resultant movies: **filter_directors.py**    
  Usage: `python filter_directors.py movies.csv directors.csv outputFile.csv`    
  
  
#### Challenge faced: 
##### Large computation time         
In many of the above filtering operations, we needed to compare two files containing a large number of lines. With two such files containing m and n tuples each, the iterative comparison through brute force lead to a time complexity of **_O(m*n)_**. Since m and n were very large, this was highly inefficient, and the system was unable to handle the computation.    

##### Approach: Increased efficiency using Hashmaps and IO buffers     
To overcome the above challenge, we used alternative approaches. We iterated over the file containing m tuples and stored the m values in hashmaps. After that, the n tuples in the other file were iterated upon and matched with the values stored in the output. This reduced the problem to **_O(m+n)_**, greatly increasing the efficiency.      
Another approach we chose is to store the input and output buffers instead of reading from and writing to files on the fly. This reduced intermittent IO time and helped increase efficiency. 

**Results:**      
After applying the above progressive filters, we obtained the following stats:    
Number of Movies: 32770     
Number of Actors: 86103    
Number of Actresses: 47143      
Number of Directors: 36248    

#### C. Data Organisation
Finally, after filtering the data and structuring it into CSV files, the data was entered into a graph database, so as to visualize the entities and their relationships. The [Neo4j](http://neo4j.com/) database was used for this purpose. Data was entered with the help of the [Cypher Query Language](http://neo4j.com/docs/stable/cypher-query-lang.html) and  the [Py2neo-2.0](http://py2neo.org/2.0/) client library in the following steps:     
  1. The *movies.csv* file was simply imported into the Neo4j database, creating a node per movie.
  2. To import actors into the database, py2neo scripts were written so as to check for each actor-movie pair, whether the node (the entity) for the actor already exists in the database. If so, the existing node for the actor was linked to the paired movie with the help of an edge (the relationship). Else, a new node was formed for the actor and a relationship was formed with the existing paired movie.
  3. Step-2 was repeated for *actresses*, *directors* and *movie-genres*.    

As a result of the above steps, we obtained a heterogeneous graph representation of the filtered data in the Neo4j database, complete with nodes representing the movies, actors, actresses, directors, and movie genres, and edges representing their corresponding relationships.

## Phase 2. Finding similar nodes
In the representation obtained in the Neo4j database, given a node in the heterogeneous graph, the objective of Phase 2 is to find the closest match for the node among the other nodes. For this, we aim to define a distance metric for two nodes of the same type, for which we will take various factors into consideration, and assign weights to each of the factors. Based on this metric, we will create a ranking of the other nodes, to represent the similarity measure. This measure will serve as the basis for finding similar nodes in the heterogeneous graph.


# Milestone 3
## Task 1
### 1. - Which services are being used for the application (described in the link above)? How do they relate to the host names in terms of computer networks?
- The application uses two services: `web` and `redis`. 
- The hostname is what a device is called on a network. `web` is the hostname of web container on the application's network. `redis` is the hostname of the redis container on the application’s network. 
- The `web` binds the container & the host machine to the exposed port `8000`. 
- The `redis` does not expose port to host.
  
### 2. - What ports are being used (within the application and in the docker-compose file)?
-  Default port for Flask web server, `5000` is used.
-  Default port for Redis, `6379` is used.

### 3. - How does the host machine (e.g. your computer) communicate with the application inside the Docker container. Which ports are exposed from the application to the host machine?
- If we want to communicate with a Docker container from our host machine, we need to have a port mapping. We open a host port to give us access to a corresponding open port inside the Docker container. Then all the requests that are made to the host port can be redirected into the Docker container.
- In this example, port `5000` is being exposed from the application to the port `8000` of host machine.

### 4. - What is localhost? Why is it useful in the domain of web applications?
A localhost is that standard hostname given to the machine itself. It is used to establish a connection with your computer using the loopback address network. The loopback address has a default IP (127.0.0.1) useful to test programs on your computer, without sending information over the internet. This helps when you are testing applications that aren’t ready for the world to see. When you call an IP address from your computer, you usually try to contact a different computer over the internet. However, with the loopback address, you are calling the localhost, aka your computer.

## Task 2 
### 1. - What is PostgreSQL? Is it SQL or no-SQL (why?)
- PostgreSQL is an open source object-relational database system that supports both SQL (relational) and JSON (non-relational) querying.
- SQL is the language used to interact PostgreSQL, (like with many others Relational database
  management system), so it is an SQL, but PostgreSQL has added support for JSON (which has been the most popular format for semi-structured data stored in NO-SQL systems)

### 2. - Create database ms3_jokes
We create `ms3_task2.py` to create and communicate with database `ms3_jokes`.

**Step 1**. Create and start containers in detached mode
```
docker-compose up -d
```
**Step 2**. Since in the `docker-compose.yml` we specify network as `app-tier` for all services, we will use
```
docker run -it --network=src_app-tier src_app bash
```
to create a new container running python script which connects to network `src_app-tier`.   

**Step 3**. Then we are in the iteractive mode of this python container. We will run the script `ms3_task2.py` by typing
```
python3 ms3_task2.py
```
**Step 4**. If we go to browser, input
```
localhost:5050
```
we will be directed to pgAdmin server. After we log in with the email address and password specified in the `docker-compose.yml`, we are able to see the GUI. 
 
**Step 5**. next, we can connect pgAdmin with postgreSQL container by fill in the IP address of postgreSQL container or hostname `db`, as well as username and password specified in  `docker-compose.yml`.
we are able to see the database `ms3_jokes`, and table `jokes`. 
If we stop and delete container, and restart container of database alone, the jokes disappear. Because we do not add `volume` to this container. However, if we add `volumes` in the docker-compose.yml, the jokes will persist. Next time when we use `docker-compose up` we will see the jokes again.

**Problems encountered:**
We tried to create table `jokes` after creating database `ms3_jokes`. However the table `jokes` is created under default database `postgres`. We spent large amount of time on googling but still have not found a perfect solution, even though we set up autocommit.
Our current solution that works is:
First, make connection to postgreSQL server and create database `ms3_jokes`, and then close connection.
Next, make connection again but to database `ms3_jokes` directly, and create table `jokes` and insert data.

## Task 3
We create `ms3_task3.py` for this this task.
### 1. - How do you need to represent/transform image data to save it to a relational database?
We transform the image data to binary string with function `dumps()` from `pickle` package and then save it in postgreSQL.
```
   insert_script = 'INSERT INTO imagesBinary(id, label, image) VALUES (%s, %s, %s) '
    for i in range(len(sample_y)):
        pickle_string_x = pickle.dumps(sample_x[i,:28,:28])  
        label = sample_y[i].tolist()
        insert_values = (i, label, pickle_string_x)
        cur.execute(insert_script, insert_values)
```
### 2. - How is your data structured?
MNIST dataset contains 60k images in training set and 10k images in testing set. 
It is downloaded with keras function and stored in four objects, i.e., 
- `x_train`: ndarray with dimension of [60000, 28, 28]
- `x_test`: ndarray with dimension of [10000, 28, 28]
- `y_train`: ndarray with dimension of [60000,]
- `y_test`: ndarray with dimension of [10000,] 

Each individual image is of dimension [28, 28], and each individual lable is of the dimension [1].
### 3. - Explain how you would define your relational database tables in terms of their attributes to save your data. What kind of data types could you use.
We define our table below
```
CREATE TABLE imagesBinary (id int PRIMARY KEY,
                           label int,
                           image bytea)
```

### 4. - What additional relational database table attributes might make sense to easily query your data (f.e. find all pictures of giraffes)?

We can add attribute `label` which represents the handwritten digit.   
If we need to retrieve first 3 images of handwritten digit 2, we can query the database by
```
SELECT image FROM imagesBinary
WHERE label = 3
LIMIT 3
```
 
### 5. - Repeat Task 2 using a sample from your own data set.
After retrieving the image data from postgreSQL, the binary data of image and label is converted back to numpy.ndarray with function `pickle.loads()` from `pickle` package. 
we are able to open image with function `Image` from `Pillow` package. We also print the data use nested for-loop below.
 
```
  cur.execute(""" SELECT * FROM  imagesBinary WHERE label=2 LIMIT 3""")
    print("Retrieve images from postgreSQL")

    for record in cur.fetchall():            
        retrieved_image = pickle.loads(record[2])
        retrieved_label = record[1]
        print(f"Image ID: {record[0]}, Label: {retrieved_label}")
        
        # Show image
        pil_image = Image.fromarray(retrieved_image)
        pil_image.show()
        
        # Alternative way to show image data
        for i in range(28):
          for j in range(28):
              print("%3d" % retrieved_image[i,j], end="")
          print("")
```


## Task 4
###  - Explain to us how you chose to structure your database (essentially your database schema). What tables do you have, what attributes do they have. 
We create `ms3_task4.py` for this task.    
ER diagram: https://drive.google.com/file/d/1FNvFEYt8WckT5l7oe4timqkjkpzjr-2J/view?usp=share_link

## Optional
### - What is an SQL Injection Attack and how can you protect yourself?
SQL injection (SQLi) is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. 
It generally allows an attacker to view data that they are not normally able to retrieve. This might include data belonging to other users, 
or any other data that the application itself is able to access. In many cases, an attacker can modify or delete this data, 
causing persistent changes to the application's content or behavior. In some situations, an attacker can escalate an SQL injection attack to 
compromise the underlying server or other back-end infrastructure, or perform a denial-of-service attack.

Some common SQL injection examples include:

- Retrieving hidden data, where you can modify an SQL query to return additional results.
- Subverting application logic, where you can change a query to interfere with the application's logic.
- UNION attacks, where you can retrieve data from different database tables.
- Examining the database, where you can extract information about the version and structure of the database.
- Blind SQL injection, where the results of a query you control are not returned in the application's responses.

Most instances of SQL injection can be prevented by using parameterized queries (also known as prepared statements) instead of string concatenation within the query.
Parameterized queries can be used for any situation where untrusted input appears as data within the query, 
including the WHERE clause and values in an INSERT or UPDATE statement. They can't be used to handle untrusted input in other parts of the query, 
such as table or column names, or the ORDER BY clause. Application functionality that places untrusted data into those parts of the query will need to take a different approach, 
such as white-listing permitted input values, or using different logic to deliver the required behavior.

For a parameterized query to be effective in preventing SQL injection, the string that is used in the query must always be a hard-coded constant, 
and must never contain any variable data from any origin. Do not be tempted to decide case-by-case whether an item of data is trusted, 
and continue using string concatenation within the query for cases that are considered safe. 
It is all too easy to make mistakes about the possible origin of data, or for changes in other code to violate assumptions about what data is tainted.

## Bonus point: 

(Wan) help solve docker network issue for Linh Ramirez's group on Slack.


## Hash digest of python packages
|Package|Version|Hash Digest|
|:------:|:---------:|------:|
|Tensorflow|2.11.0|d973458241c8771bf95d4ba68ad5d67b094f72dd181c2d562ffab538c1b0dad7|
|numpy|1.23.5|f9a909a8bae284d46bbfdefbdd4a262ba19d3bc9921b1e76126b1d21c3c34135|
|psycopg2|2.9.5|920bf418000dd17669d2904472efeab2b20546efd0548139618f8fa305d1d7ad|
|Pillow|9.3.0|0b07fffc13f474264c336298d1b4ce01d9c5a011415b79d4ee5527bb69ae6f65|

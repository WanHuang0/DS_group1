TASK 1
-
Which services are being used for the application (described in the link above)? How do they relate
to the host names in terms of computer networks?
- application uses two services: web and redis 
- the web is building an image and binding the container & the host machine to the exposed port 8000
- the redis uses Redis image pulled from the docker hub registry 
  
What ports are being used 
(within the application and in the docker-compose file)?
- ports 8000 and 5000 are being used within the application 

How does the host machine (e.g. your computer) communicate 
  with the application inside the
Docker container. Which ports are exposed from the application to the host machine?
- port 5000 is being exposed from the application to the host machine via localhost 8000

What is localhost, why is it useful in the domain
  of web applications?
- localhost is the (host name) of the computer that is executing a program 
- it is useful for making loopback requests to person's own device which is 
particularly 
  useful for testing and security reasons


TASK 2 
-

What is PostgreSQL?

- PostgreSQL is an open source object-relational database system that supports both SQL (relational)
  and JSON (non-relational) querying
- SQL is the language used to interact PostgreSQL, (like with many others Relational database
  management system), so it is an SQL, but 
  PostgreSQL has added support for JSON (which has been the most popular format for semi-structured data stored in NO-SQL systems)
  

TASK 3
-


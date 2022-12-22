from psycopg2 import connect, extensions

# Setup
hostname = 'db'
port_id = '5432' 
username = 'postgres'
pwd = 'admin'
dbname = 'ms3_jokes'
conn = None
cur = None

try:
    # Establishing the connection
    conn = connect(
        host = hostname,
        user = username,
        password = pwd, 
        port = port_id )
    
    # Set autocommit
    auto_commit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    conn.set_isolation_level(auto_commit)
    
    # Creating a cursor object to perform database operations
    cur = conn.cursor()
    
    # Check whether we are able to perform database operations
    print("Cursor found",cur)
  
    # Create a database named 'ms3_jokes'
    create_db = '''CREATE DATABASE ms3_jokes'''
    cur.execute(create_db)
    
except Exception as error:
    print(error)
    
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
         
try:
    # Establishing the connection
    conn = connect(
        host = hostname,
        user = username,
        password = pwd, 
        port = port_id,
        dbname = dbname)
    
    # Set autocommit
    auto_commit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    conn.set_isolation_level(auto_commit)
    
    # Creating a cursor object to perform database operations
    cur = conn.cursor()        
    
    # Create a table named 'jokes'
    create_tb = '''CREATE TABLE jokes  (
                        id int PRIMARY KEY,
                        JOKE TEXT )'''
    cur.execute(create_tb)
    
    # Insert records into table 'jokes'
    insert_script = 'INSERT INTO jokes(id, JOKE) VALUES (%s, %s) '
    insert_values = [(1, "- Tell me a joke. - My life"),(2, "Q: 0 is false and 1 is true, right?A: 1")]
    for record in insert_values:
        cur.execute(insert_script, record)
    
    # Fetch records from table 'jokes'
    cur.execute(""" SELECT * from jokes """)
    for record in cur.fetchall():
        print(record)

except Exception as error:
    print(error)
    
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    
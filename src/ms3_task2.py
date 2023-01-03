from psycopg2 import connect, extensions

# Setup
hostname = 'db'
port_id = '5432' 
username = 'postgres'
pwd = 'admin'
dbname = 'ms3_jokes'
conn = None
cur = None

# Create database
def CreateDB(dbname):
    '''
    Create database
    
    dbname (string): database name
    '''
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
        
        # Create a new database if it does not exist
        # query = '''SELECT * FROM pg_catalog.pg_database WHERE datname="mnist"'''
        cur.execute(f"SELECT * FROM pg_catalog.pg_database WHERE datname='{dbname}'")
        exists = cur.fetchall()
        if exists:      
            print(f"Database {dbname} already exists")
        else:
            # Create a database
            create_db = '''CREATE DATABASE ''' +  dbname
            cur.execute(create_db)
            print(f"Successfully create a new database {dbname}")
        
    except Exception as error:
        print(error)
        
    finally:
        # Close cursor and connection
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
            
# Create database 
CreateDB(dbname)

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
    
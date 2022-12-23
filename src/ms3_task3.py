from psycopg2 import connect, extensions
from tensorflow import keras
from PIL import Image 
import pickle

hostname = 'db'
port_id = '5432' 
username = 'postgres'
pwd = 'admin'
dbname = 'mnist'
conn = None
cur = None

# Load data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# Take a sample
sample_x = x_train[:200, :28, :28]
sample_y = y_train[:200]

# create database 
def CreateDB(dbname):
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
        
        # Create a database
        create_db = '''CREATE DATABASE ''' +  dbname
        cur.execute(create_db)
        print(f"Successfully create a database {dbname}")
        
    except Exception as error:
        print(error)
        
    finally:
        # Close cursor and connection
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

# Create database mnist
CreateDB(dbname)

# Create table
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

    # Check whether we are able to perform database operations
    print("Cursor found",cur)
                    
    # Create table
    create_tb = '''CREATE TABLE imagesBinary (
                        id int PRIMARY KEY,
                        label int,
                        image bytea)'''
    
    cur.execute(create_tb)
    print("Successfully create table imagesBinary")
    
    # Transform ndarray to binary data and insert records to postgreSQL
    insert_script = 'INSERT INTO imagesBinary(id, label, image) VALUES (%s, %s, %s) '
    for i in range(len(sample_y)):
        pickle_string_x = pickle.dumps(sample_x[i,:28,:28])  
        label = sample_y[i].tolist()
        insert_values = (i, label, pickle_string_x)
        cur.execute(insert_script, insert_values)
    print("Successfully insert image data into table imagesBinary")
    
    # Fetch data from postgreSQL
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

except Exception as error:
    print(error)
    
finally:
    # Close cursor and connection
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()







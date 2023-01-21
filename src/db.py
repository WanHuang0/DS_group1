from psycopg2 import connect, extensions
from tensorflow import keras
import pickle
import numpy as np
import data_process 

# Setup
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
sample_x = x_train[0, :28, :28]
sample_y = y_train[0]

# Create database
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

# Create tables
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
    
    # Create table input_data
    create_tb1 = '''CREATE TABLE IF NOT EXISTS input_data (
                        id SERIAL PRIMARY KEY,
                        image bytea)'''
    
    cur.execute(create_tb1)
    print("Successfully created table input_data")


    # Create table predictions
    create_tb2 = '''CREATE TABLE IF NOT EXISTS predictions (
                        pred_id SERIAL PRIMARY KEY REFERENCES input_data(id),
                        prediction int)'''
    
    cur.execute(create_tb2)
    print("Successfully created table prediction")
    
except Exception as error:
    print(error)
    
finally:
    # Close cursor and connection
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


# Insert values of input data
def insert_input(input_data):
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
        
        # Transform ndarray to binary data and insert data to table input_data
        insert_script1 = 'INSERT INTO input_data(image) VALUES (%s) ON CONFLICT (id) DO NOTHING'
        
        pickle_string_x = pickle.dumps(input_data)  
        # label = sample_y[i].tolist()
        insert_values1 = (pickle_string_x,)
        cur.execute(insert_script1, insert_values1)
        print("Successfully inserted image data into table input_data")   
    
    except Exception as error:
        print(error)
        
    finally:
        # Close cursor and connection
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
 
    
# Insert values of prediction
def insert_prediction(prediction):
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

        # Store prediction results into table predictions
        insert_script2 = 'INSERT INTO predictions(prediction) VALUES (%s)'
        prediction = prediction.tolist()
        insert_values2 = (prediction,)
        cur.execute(insert_script2, insert_values2)
        print("Successfully inserted prediction into table predictions")
    
    
    except Exception as error:
        print(error)
        
    finally:
        # Close cursor and connection
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


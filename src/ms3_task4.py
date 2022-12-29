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
dbname = 'milestone_3'
conn = None
cur = None

# Load data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# Take a sample
sample_x = x_train[:200, :28, :28]
sample_y = y_train[:200]

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
                        id int PRIMARY KEY,
                        label int,
                        image bytea)'''
    
    cur.execute(create_tb1)
    
    # Transform ndarray to binary data and insert data to table input_data
    insert_script1 = 'INSERT INTO input_data(id, label, image) VALUES (%s, %s, %s) '
    for i in range(len(sample_y)):
        pickle_string_x = pickle.dumps(sample_x[i,:28,:28])  
        label = sample_y[i].tolist()
        insert_values1 = (i, label, pickle_string_x)
        cur.execute(insert_script1, insert_values1)
    print("Successfully inserted image data into table input_data")

    # Create table predictions
    create_tb2 = '''CREATE TABLE IF NOT EXISTS predictions (
                        pred_id int REFERENCES input_data(id),
                        prediction bytea)'''
    
    cur.execute(create_tb2)
    
    # Fetch input data from postgreSQL
    cur.execute(''' SELECT * FROM  input_data WHERE label = 2''')
    records = cur.fetchall()
    print("Retrieve images from postgreSQL")
    
    retrieved_image = np.array([[[0] * 28] * 28]*len(records))
    retrieved_id = np.array([0]*len(records))
    for i in range(len(records)):
        retrieved_image[0] = pickle.loads(records[i][2])
        retrieved_id[i] = records[i][0]
    
    # Load trained model
    model_nn = trained_model = keras.models.load_model("/model/model_nn.h5")
    print("Load the model")
    
    # Process input data
    x_pred = data_process.scale(retrieved_image)
    # print(x_pred[0])
    
    # Make prediction
    y_pred = trained_model.predict(x_pred)
    print("Successfully made prediction")
    
    # Store prediction results into table predictions
    insert_script2 = 'INSERT INTO predictions(pred_id, prediction) VALUES (%s, %s)'
    
    for i in range(len(y_pred)):
        pickle_string_y2 = pickle.dumps(y_pred[i,:10])         
        insert_values2 = (retrieved_id[i].tolist(), pickle_string_y2)
        cur.execute(insert_script2, insert_values2)
    print(f"Successfully inserted {len(y_pred)} predictions into table predictions")


except Exception as error:
    print(error)
    
finally:
    # Close cursor and connection
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()



 
    

    




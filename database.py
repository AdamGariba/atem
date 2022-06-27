import sqlite3
from sqlite3 import Error

from atem.config import DATABASE

# Get a connection to the database
def create_connection():
    conn = None

    try:
        conn = sqlite3.connect(f"{DATABASE}")
    except Error as e:
        print(e)
    
    return conn


# Initialize the database (Create table and insert test data)
def init_db(printTable=False):
    conn = create_connection()

    # Call schema script
    with open("./misc/schema.sql", 'r') as fin:
        sqlScript = fin.read()
        conn.executescript(sqlScript)
    
    # commit changes
    conn.commit()

    # Print rows in table
    if printTable is True:
       for row in conn.execute("SELECT * FROM ANIME"):
           print(row)

    


    
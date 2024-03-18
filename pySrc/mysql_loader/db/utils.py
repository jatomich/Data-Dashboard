# description: This file contains the functions to connect to the database, create a database, import a csv file to a table, and execute a query.
# Author: Andrew Tomich

import os

import mysql.connector
from mysql.connector import errorcode

import pandas as pd

USER = os.environ.get('MYSQL_USER', None)
PASSWORD = os.environ.get('MYSQL_PASSWORD', None)
HOST = os.environ.get('MYSQL_HOST', None)
PORT = int(os.environ.get('MYSQL_PORT', None))
DB_NAME = os.environ.get('MYSQL_DB_NAME', None)
CNNXN_CONFIG = {
    'user': USER,
    'password': PASSWORD,
    'host': HOST,
    'port': PORT,
    'database': None
}


def connect_to_database():
    """
    Connects to the MySQL database.

    Returns:
        tuple: A tuple containing the connection object and the cursor object.
    """
    # connect to the database using the mysql.connector.connect method and acquire a connection object.
    cnnxn = mysql.connector.connect(**CNNXN_CONFIG)

    # acquire a cursor object from the connection object.
    cursor = cnnxn.cursor()

    return cnnxn, cursor


def create_or_use_database(cursor, cnnxn):
    """
    Creates or uses the specified database.

    Args:
        cursor: The cursor object.
        cnnxn: The connection object.

    Returns:
        None
    """
    try:
        # use the specified database, if it exists.
        cursor.execute(f"USE {DB_NAME}")

    # catch any mysql.connector.Error exceptions.
    except mysql.connector.Error as err:
        print(f"Database {DB_NAME} does not exist.")

        # if the exception is a 'bad database' error, create the database.
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print(f"Database {DB_NAME} created successfully.")
            
            # use the newly created database.
            cnnxn.database = DB_NAME
        # if the exception is not a 'bad database' error,
        # print the error and exit the program.
        else:
            print(err)
            exit(1)


def create_database(cursor):
    """
    Creates a new database.

    Args:
        cursor: The cursor object.

    Returns:
        None
    """
    # create a new database using the cursor's execute method.
    try:
        cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'"
            )
    # catch any mysql.connector.Error exceptions, print the error to stdout, and exit the program with an error code of 1.
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)


def import_csv_to_table(engine, csv_file, table_name):
    """
    Imports a CSV file into a database table.

    Args:
        engine (sqlalchemy.engine.Engine): The database engine.
        csv_file (str): The path to the CSV file.
        table_name (str): The name of the table to import the data into.

    Returns:
        None
    """
    # Read a CSV file into a pandas DataFrame.
    if csv_file.endswith('.csv'):
        df = pd.read_csv(csv_file,
                         low_memory=False)

    # Read a TSV file into a pandas DataFrame.
    if csv_file.endswith('.tsv'):
        df = pd.read_csv(csv_file,
                         sep='\t',
                         low_memory=False)

    # Read an XLSX file into a pandas DataFrame.
    if csv_file.endswith('.xlsx'):
        df = pd.read_excel(
            io=csv_file,
            engine='openpyxl')

    ######################
    ##  Clean the data  ##
    ######################

    # Fill all NaN values with an empty string.
    df = df.fillna('')
    df = df.replace('\\N', '')

    # Convert all string columns to lowercase.
    for column in df.columns:
        df[column] = df[column].map(lambda x: x.lower() if type(x) == str else x)

    # Remove any double quotes from the 'cast' and 'description' columns in the 'netflix_titles.csv' file.
    if csv_file.lower() == 'netflix_titles.csv':
        df.loc[(df['cast'].str.contains('\"')) | (df['description'].str.contains('\"')), ['cast', 'description']] = df.loc[(df['cast'].str.contains('\"')) | (df['description'].str.contains('\"')), ['cast', 'description']].apply(lambda x: x.replace('\"', ''))

    # If the current file is 'netflixdump.csv', remove any text after the '//' in the 'title' column.
    if 'dump' in csv_file.lower():
        df['title'] = df['title'].map(lambda x: x.split('//')[0].strip() if '//' in x else x)

    # insert data into the table using the pandas to_sql method.
    df.to_sql(name=table_name,
              con=engine,
              if_exists="replace",
              index=False,
              method='multi',
              chunksize=1000,
              )
    

def execute_query(cursor, query):
    """
    Executes the given query using the provided cursor.

    Args:
        cursor: The cursor object to execute the query with.
        query: The SQL query to be executed.

    Raises:
        mysql.connector.Error: If an error occurs while executing the query.

    Returns:
        None
    """
    try:
        # execute the query using the cursor's execute method.
        cursor.execute(query)

    # catch any mysql.connector.Error exceptions.
    except mysql.connector.Error as err:

        # if the exception is a 'table exists' error, print "already exists." to stdout.
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")

        # print all errors to stdout.
        print(err.msg)
    else:
        # if the query is successful, print "OK" to stdout.
        print("OK")
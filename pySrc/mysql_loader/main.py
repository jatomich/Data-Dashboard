# description: This script connects to a MySQL database, creates or uses an existing database
# Author: Andrew Tomich

from __future__ import print_function

from db.utils import (
    USER, PASSWORD,
    HOST, PORT, DB_NAME,
    connect_to_database,
    create_or_use_database,
    execute_query,
    import_csv_to_table
)
from db.tables import table_list

from sqlalchemy import create_engine


def main():
    """
    This script connects to a MySQL database, creates or uses an existing database,
    executes queries to create tables, and imports CSV files into the tables.
    """

    # Connect to the database, and acquire 'cnnxn' and 'cursor' objects.
    # Next, we'll pass the 'cursor' and 'cnnxn' objects to the 'create_or_use_database' function
    # so that we can interact with the database (e.g. create a new database, or use an existing one).
    cnnxn, cursor = connect_to_database()
    create_or_use_database(cursor, cnnxn)

    # Use the 'cursor' to create the tables defined in 'table_list' from 'db/tables.py'.
    for table in table_list:
        execute_query(cursor, table.values())

    # create a sqlalchemy engine object to connect to the database.
    engine = create_engine(f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')

    # Use the sqlalchemy engine's connection to import the CSV files into the tables.
    import_csv_to_table(engine, '../data/netflix_final.xlsx', 'netflix_combined')
    import_csv_to_table(engine, '../data/imdb_tconst.xlsx', 'imdb_combined')
    import_csv_to_table(engine, '../data/imdbtitles.xlsx', 'imdb_titles')
    import_csv_to_table(engine, '../data/imdbratings.xlsx', 'imdb_ratings')
    import_csv_to_table(engine, '../data/NetflixDump.csv', 'netflix_dump')
    import_csv_to_table(engine, '../data/netflix_titles.csv', 'netflix_titles')

    # Commit the changes and close the connection.
    cnnxn.commit()
    cursor.close()
    cnnxn.close()


if __name__ == '__main__':
    main()


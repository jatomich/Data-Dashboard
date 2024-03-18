import pandas as pd
import requests
import json


def pb_load(filename: str='../data/FULLY_COMBINED_DATASET.xlsx',
            collection: str='NetflixIMDb'
            ) -> None:

    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(
        filename,
        usecols=[
            'tconst',
            'title',
            'releaseYear',
            'runtimeMinutes',
            'genres',
            'averageRating',
            'numVotes',
            'type'
            ]
        )

    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict('records')

    # Define the API endpoint for checking the collection
    url_check_collection = f'http://127.0.0.1:8090/api/collections/{collection}'

    # Send a GET request to check if the collection exists
    response_check_collection = requests.get(url_check_collection)

    # If the collection doesn't exist, create it
    if response_check_collection.status_code == 404:
        response_create_collection = requests.post(url_check_collection)
        if response_create_collection.status_code != 200:
            print(f"Failed to create collection: {response_create_collection.text}")
        else:
            print("Collection created successfully")

    # Define the API endpoint for sending the data
    url = f'http://127.0.0.1:8090/api/collections/{collection}/records'

    # Send the data to the Pocketbase database
    for i, record in enumerate(data):
        response = requests.post(url, data=json.dumps(record), headers={'Content-Type': 'application/json'})

        # Check the response
        if response.status_code != 200:
            print(f"Failed to post record: {response.text}")

        if i % 5 == 0:
            print(f"Posted {i} records")


if __name__ == '__main__':
    filepath = input("Enter the path to the Excel file: ")
    collection = input("Enter the name of the collection: ")
    pb_load(filepath, collection)
# -*- coding: utf-8 -*-
from dotenv import find_dotenv, load_dotenv
import pandas as pd
import os
from sas.gcp import bigquery, storage
import tempfile
from google.oauth2 import service_account

def main():
    """ Runs python file to get data from bigquery (or other source)
        and save data ready to be processed (feature engeneering) in
        (data/raw/)
    """

# load environment variables
load_dotenv(verbose=True)

CREDENTIALS = os.getenv("GCP_CREDENTIALS")
PROJECT_ID_BQ = os.getenv("PROJECT_ID_BQ")
BUCKET = os.getenv("BUCKET_NAME")
PROJECT_ID_GS = os.getenv("PROJECT_ID_GS")
ENV = os.getenv("ENV")
SERVICE_ACCOUNT = os.getenv('SERVICE_ACCOUNT')

# query data
credentials = pydata_google_auth.load_user_credentials(CREDENTIALS)
service_credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT)
project_id=PROJECT_ID_BQ
client = storage.Storage(credentials=service_credentials, project_id=PROJECT_ID_GS)

with open("src/data/get_data.sql") as file:
    query = file.read()

client = bigquery.Bigquery(credentials=credentials, project_id=project_id)
df = client.get_data(query)
print("done querying...")


if ENV == "local":
    df.to_csv("data/raw/raw_data.csv", index=False, sep=",")

elif ENV == 'dev':
    client = storage.Storage(credentials=service_credentials, project_id=PROJECT_ID_GS)

    with tempfile.TemporaryDirectory() as tempdir:
        tmp_path = tempdir + '/raw_data.csv'
        df.to_csv(tmp_path)
        teste = pd.read_csv(tmp_path)
        print(teste.head())
        client.save_file(bucket_name=BUCKET,
                         blob_path='data/raw/raw_data.csv',
                         source_file_name=tmp_path)

elif ENV == 'prod':
    pass




if __name__ == '__main__':

    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


try:
    uri = os.environ.get("MYAPP_CONNECTION_STRING")
    client = MongoClient(uri)
    database = client["Contabil"]
    collection = database["notas"]
    # start example code here
    print(collection.find_one({ "title" : "NOTA 1" }))
    # end example code here
    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
uri = os.environ.get("MYAPP_CONNECTION_STRING")
client = MongoClient(uri)
database = client["Contabil"]


def insert_nf(data, database):
        collections= database["Contabil"]
        collections.insert_one(data)
        print("Nota Fiscal inserida com sucesso")

def find_nf(data, database):
        collections= database["Contabil"]
        return collections.find_one(data)

def excluir_nf(data, database):
        collections= database["Contabil"]
        collections.delete_one(data)
        client.close()
        print("Nota Fiscal excluida com sucesso")

def atualizar_nf(data, database):
        collections= database["Contabil"]
        collections.update_one(data)
        client.close()
        print("Nota Fiscal atualizada com sucesso")


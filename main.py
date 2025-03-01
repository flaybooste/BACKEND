from dotenv import load_dotenv
from flask import Flask, request, jsonify
import db
from db import insert_nf


load_dotenv()
app = Flask(__name__)
app.config.from_prefixed_env("MYAPP")



@app.route("/api/v1/insertnf", methods=["POST"])
def insert():
    data = request.json
    insert_nf(data, db.database)
    return jsonify(data)


app.run(port=5000, debug=True)

from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongo', 27017)
db = client.mydatabase

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    db.mycollection.insert_one(data)
    return jsonify({"message": "Data stored successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

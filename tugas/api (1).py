from flask import Flask, request, jsonify
import json

app = Flask(__name__)

USERS = "users.json"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    with open(USERS) as f:
        users = json.load(f)

    for u in users:
        if u["username"] == data["username"] and u["password"] == data["password"]:
            return jsonify({"status": "success"})

    return jsonify({"status": "failed"})

app.run(port=5000)
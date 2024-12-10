from flask import Flask, jsonify, request
import random

app = Flask(__name__)

ROLES = ["Мафия", "Мирный житель", "Детектив", "Доктор"]

@app.route("/role", methods=["GET"])
def get_role():
    role = random.choice(ROLES)
    return jsonify({"role": role})

@app.route("/podcast", methods=["GET"])
def podcast():
    return jsonify({"link": "https://example.com/sport-mafia-podcast"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

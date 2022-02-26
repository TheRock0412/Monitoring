import pymongo
from pymongo import MongoClient
from flask import Flask, redirect, render_template

app = Flask(__name__)

#Routes
from versuch import user_routes

#Start der MongoDB und connection
#Commandline eingabe: brew services start mongodb-community
client = pymongo.MongoClient("mongodb://localhost:27017")
print(client.list_database_names())

#db = client["pi_db"]
#col = db["users"]
db = client.pi_db

#user = {
#    "_id": '1',
#    "name": 'name',
#    "email": 'email2',
#    "password": 'password'
#    }
#col.insert_one(user)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

# @app.route('/add_Pi')
# def home():
#     return render_template('addPi.html')

if __name__ == "__main__":
    app.run(debug=True)

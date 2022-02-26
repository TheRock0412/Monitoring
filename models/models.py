from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
from app import db
import uuid

class User:
    def signup(self):
        print(request.form)

        #Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }
        #Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        print("User Class")
        #Check for existing email address
        if db.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use!"}), 400

        if db.insert_one(user):
            return jsonify(user), 200

        return jsonify({"error": "Signup failed"}), 400

# class Pi:
#     def distribution():
#
#         #Create the Pi object
#         pi = {
#             "_id": puid,
#             "hostname": request.from.get('hostname'),
#             "ip": request.from.get('ip'),
#             "user": request.from.get('user'),
#             "password": request.from.get('password')
#         }
#         #Encrypt the password
#         pi['password'] = pbkdf2_sha256.encrypt(user['password'])
#
#         #Check for existing email address
#         if db.pis.find_one({"ip": pi['ip']}):
#             return jsonify({"error": "IP address is already existing!"}), 400
#
#         return jsonify(pi), 200

import random
from flask import Flask, request
from models.User import User

app = Flask(__name__)

users: list[User] = []

@app.route('/')
def index():
    return 'Hello from Users CRUD example'

@app.route('/users', methods=['GET'])
def get_users():
    return [user.__dict__ for user in users]

@app.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id: str):
    is_found = None
    for user in users:
        if user.id == user_id:
            is_found = user
    if not is_found:
        return {"message": f"user with id {user_id} not found"} , 404
    return is_found.__dict__


@app.route('/users', methods=['POST'])
def create_users():
    params = {
        "id": str(random.randint(900000000, 999999999)),
        "name": request.json['name'],
        "email": request.json['email'],
    }
    new_user = User(params['id'], params['name'], params['email'])
    users.append(new_user)
    return params

@app.route('/users/<user_id>', methods=['PUT'])
def update_users(user_id: str):
    params = {
        "id": user_id,
        "name": request.json['name'],
        "email": request.json['email'],
    }
    is_found = None
    for user in users:
        if user.id == user_id:
            user.name = params['name']
            user.email = params['email']
            is_found = user
    if not is_found:
        return {"message": f"user with id {user_id} not found"} , 404
    return params

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_users(user_id: str):
    is_found = None
    for user in users:
        if user.id == user_id:
            is_found = user
    if not is_found:
        return {"message": f"user with id {user_id} not found"} , 404
    users.remove(is_found)
    return is_found.__dict__

app.run(port=3000, debug=True)

from flask import Blueprint, jsonify
from user.src.model import User, UserSerializer


users = Blueprint('users', __name__)

@users.route('/')
def list_users():
    users = User.query.all()
    return jsonify(UserSerializer(users).data)

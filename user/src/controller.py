from flask import Blueprint, jsonify, request
from user.src.model import User, UserSerializer


users = Blueprint('users', __name__)

@users.route('/')
def list_users():
    users = User.query.all()
    return jsonify(UserSerializer(users).data)


@users.route('/', methods=['POST'])
def create_user():
    name = request.json.get('name', None)

    if not name:
        return jsonify(message='name parameter missing'), 403

    user = User(name=name).save()

    return jsonify(UserSerializer(user).data), 201
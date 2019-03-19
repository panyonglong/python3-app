import json

from flask import Blueprint, request
from common.utils.result import Result
from platform.model.user import User
from platform.cache import redis


user = Blueprint('user', __name__)


@user.route('', methods=['GET', 'POST'])
def index():
    list = User.query.all()
    data = {
        'list': [{'name':x.name, 'email':x.email, 'id':x.id} for x in list]
    }
    rr = redis.get('test')
    print(rr)
    redis.set('test', json.dumps(data), ex=10)
    
    return Result(0, "", data).toDict()

@user.route('/add', methods=['GET', 'POST'])
def add():
    name = request.values.get('name', '')
    email = request.values.get('email', '')
    user = User(name = name, email = email)
    user.save()
    return Result(0, "").toDict()

@user.route('/<int:id>', methods=['GET', 'POST'])
def info(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return "{}"
    data = {'name':user.name, 'email':user.email, 'id': user.id}
    return Result(0, "", data).toDict()

@user.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    name = request.values.get('name', '')
    email = request.values.get('email', '')

    user = User.query.filter_by(id=id).first()
    user.name = name
    user.email = email
    user.save();
    return Result(0, "").toDict()

@user.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):

    user = User.query.filter_by(id=id).first()
    user.delete();
    return Result(0, "").toDict()

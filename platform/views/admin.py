import json

from flask import Blueprint, request
from common.utils.result import Result
from platform.model.admin import Admin


admin = Blueprint('admin', __name__)



@admin.route('', methods=['GET', 'POST'])
def index():
    list = Admin.query.all()
    data = {
        'list': [{'name':x.name, 'email':x.email, 'id':x.id} for x in list]
    }
    return Result(0, "", data).toDict()

@admin.route('/add', methods=['GET', 'POST'])
def add():
    name = request.values.get('name', '')
    email = request.values.get('email', '')
    admin = Admin(name = name, email = email)
    admin.save()
    return Result(0, "").toDict()

@admin.route('/<int:id>', methods=['GET', 'POST'])
def info(id):
    admin = Admin.query.filter_by(id=id).first()
    if admin is None:
        return "{}"
    data = {'name':admin.name, 'email':admin.email, 'id': admin.id}
    return Result(0, "", data).toDict()

@admin.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    name = request.values.get('name', '')
    email = request.values.get('email', '')

    admin = Admin.query.filter_by(id=id).first()
    admin.name = name
    admin.email = email
    admin.save();
    return Result(0, "").toDict()

@admin.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):

    admin = Admin.query.filter_by(id=id).first()
    admin.delete();
    return Result(0, "").toDict()

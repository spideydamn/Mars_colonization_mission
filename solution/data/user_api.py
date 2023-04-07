# -*- coding: cp1251 -*-

import flask
from flask import jsonify, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/user')
def get_user():
    db_sess = db_session.create_session()
    user = db_sess.query(User).all()
    return jsonify(
        {
            'user':
                [item.to_dict(only=("id", "surname", "name", "age", "position", "speciality", "address", "email",
                                    "hashed_password", "modified_date")) for item in user]
        }
    )


@blueprint.route('/api/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'user': user.to_dict(only=("id", "surname", "name", "age", "position", "speciality", "address", "email",
                                       "hashed_password", "modified_date"))
        }
    )


@blueprint.route('/api/user', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ["id", "surname", "name", "age", "position", "speciality", "email",
                  "password", "modified_date"]):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if not db_sess.query(User).get(request.json["id"]):
        user = User()
        user.surname = request.json["surname"]
        user.name = request.json["name"]
        user.age = request.json["age"]
        user.position = request.json["position"]
        user.speciality = request.json["speciality"]
        if "address" in request.json:
            user.address = request.json["address"]
        user.email = request.json["email"]
        user.set_password(request.json["password"])
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    return jsonify({'error': 'Id already exists'})


@blueprint.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/user', methods=['PUT'])
def put_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ["id"]):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if db_sess.query(User).get(request.json["id"]):
        user = db_sess.query(User).get(request.json["id"])
        if "surname" in request.json:
            user.surname = request.json["surname"]
        if "name" in request.json:
            user.name = request.json["name"]
        if "age" in request.json:
            user.age = request.json["age"]
        if "position" in request.json:
            user.position = request.json["position"]
        if "speciality" in request.json:
            user.speciality = request.json["speciality"]
        if "address" in request.json:
            user.address = request.json["address"]
        if "email" in request.json:
            user.email = request.json["email"]
        if "password" in request.json:
            user.set_password(request.json["password"])
        db_sess.commit()
        return jsonify({'success': 'OK'})
    return jsonify({'error': 'Id does not exist'})
# -*- coding: cp1251 -*-

import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=("id", "team_leader", "job", "work_size", "collaborators", "start_date",
                                    "end_date", "is_finished")) for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': job.to_dict(only=("id", "team_leader", "job", "work_size", "collaborators", "start_date",
                                      "end_date", "is_finished"))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ["id", "team_leader", "job", "work_size", "collaborators", "is_finished"]):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if not db_sess.query(Jobs).get(request.json["id"]):
        job = Jobs()
        job.id = request.json["id"]
        job.team_leader = request.json["team_leader"]
        job.job = request.json["job"]
        job.work_size = request.json["work_size"]
        job.collaborators = request.json["collaborators"]
        job.is_finished = request.json["is_finished"]
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    return jsonify({'error': 'Id already exists'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs', methods=['PUT'])
def put_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ["id"]):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if db_sess.query(Jobs).get(request.json["id"]):
        job = db_sess.query(Jobs).get(request.json["id"])
        if "team_leader" in request.json:
            job.team_leader = request.json["team_leader"]
        if "job" in request.json:
            job.job = request.json["job"]
        if "work_size" in request.json:
            job.work_size = request.json["work_size"]
        if "collaborators" in request.json:
            job.collaborators = request.json["collaborators"]
        if "is_finished" in request.json:
            job.is_finished = request.json["is_finished"]
        db_sess.commit()
        return jsonify({'success': 'OK'})
    return jsonify({'error': 'Id does not exist'})
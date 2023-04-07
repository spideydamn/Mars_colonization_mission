# -*- coding: cp1251 -*-

from requests import get, post

print(post('http://localhost:5000/api/jobs').json()) # запроса в виде json нет

print(post('http://localhost:5000/api/jobs',
           json={'job': 'Заголовок'}).json()) # не все параметры работы в json есть

print(post('http://localhost:5000/api/jobs',
           json={"id": 12, "team_leader": "1", "job": "new_job", "work_size": 12,
                 "collaborators": "1, 2, 3", "is_finished": False}).json()) # все хорошо

print(post('http://localhost:5000/api/jobs',
           json={"id": 12, "team_leader": "1", "job": "new_job", "work_size": 12,
                 "collaborators": "1, 2, 3", "is_finished": False}).json()) # с таким id работа уже существует

# print(get('http://localhost:5000/api/jobs').json())
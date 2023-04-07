# -*- coding: cp1251 -*-

from requests import get, post, delete, put

print(delete('http://localhost:5000/api/jobs/1'))

print(post('http://localhost:5000/api/jobs',
           json={"id": 1, "team_leader": "1", "job": "new_job", "work_size": 12,
                 "collaborators": "1, 2, 3", "is_finished": False}).json())

print(get('http://localhost:5000/api/jobs').json())


print(put('http://localhost:5000/api/jobs',
           json={"id": 1, "team_leader": "2", "job": "new_job_2", "work_size": 15,
                 "collaborators": "4, 5, 6", "is_finished": True}).json())

print(get('http://localhost:5000/api/jobs').json())


print(put('http://localhost:5000/api/jobs',
           json={"id": 1, "team_leader": "1", "job": "new_job", "work_size": 12,
                 "collaborators": "1, 2, 3", "is_finished": False}).json())

print(get('http://localhost:5000/api/jobs').json())


print(delete('http://localhost:5000/api/jobs/123321'))

print(put('http://localhost:5000/api/jobs',
           json={"id": 123321, "team_leader": "1", "job": "new_job", "work_size": 12,
                 "collaborators": "1, 2, 3", "is_finished": False}).json())

# -*- coding: cp1251 -*-

from requests import get, post, delete

print(post('http://localhost:5000/api/jobs',
           json={"id": 12, "team_leader": "1", "job": "new_job", "work_size": 12,
                 "collaborators": "1, 2, 3", "is_finished": False}).json())

print(get('http://localhost:5000/api/jobs').json())

print(delete('http://localhost:5000/api/jobs/999123').json())

print(get('http://localhost:5000/api/jobs').json())

print(delete('http://localhost:5000/api/jobs/12').json())

print(get('http://localhost:5000/api/jobs').json())
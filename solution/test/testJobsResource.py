# -*- coding: cp1251 -*-

from requests import get, post, delete, put

print(post('http://localhost:5000/api/v2/jobs',
           json={"team_leader": "1", "job": "new_job"}).json())
print(post('http://localhost:5000/api/v2/jobs',
           json={"team_leader": "1", "job": "new_job", "work_size": 12,
                 "collaborators": "1, 2, 3", "is_finished": False}).json())
print(get("http://localhost:5000/api/v2/jobs").json())
print(delete('http://localhost:5000/api/v2/jobs/1').json())
print(delete('http://localhost:5000/api/v2/jobs/1').json())
print(get("http://localhost:5000/api/v2/jobs").json())
print(get("http://localhost:5000/api/v2/jobs/1").json())


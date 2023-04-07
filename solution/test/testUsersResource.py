# -*- coding: cp1251 -*-

from requests import get, post, delete, put

print(post('http://localhost:5000/api/v2/user',
           json={'name': 'Denchik', 'surname': 'Yavor'}).json())
print(post('http://localhost:5000/api/v2/user',
           json={'address': 'module_228', 'age': 17, 'email': 'yavor_denchik@mars.org', 'password': '123321',
                 'name': 'Denchik', 'position': 'captain', 'speciality': 'software engineer',
                 'surname': 'Yavor'}).json())
print(get("http://localhost:5000/api/v2/user").json())
print(delete('http://localhost:5000/api/v2/user/1').json())
print(delete('http://localhost:5000/api/v2/user/1').json())
print(get("http://localhost:5000/api/v2/user").json())
print(get("http://localhost:5000/api/v2/user/1").json())

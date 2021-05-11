import requests
from requests.auth import HTTPBasicAuth

response = requests.put('http://127.0.0.1:8000/people/3/', auth=HTTPBasicAuth('admin','jebacdisa1') , data={
    "first_name": "Janina",
    "last_name": "Nowak",
    "gender": "female",
    "occupation": "mechanic"
}
)
print(response.headers)
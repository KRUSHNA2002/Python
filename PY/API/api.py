import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
)

print(response.status_code)
data=response.json()

for user in data:
    print(f"{'name ->', user['name']},'\nemail - >' {user['email']},'\ncity ->' {user["address"]["city"]}\n")
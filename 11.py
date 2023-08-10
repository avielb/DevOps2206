import requests
response = requests.get("https://api.github.com/users/avielb/repos")
repositories = response.json()

for repo in repositories:
    if "DEVOPS" in repo["name"].upper():
        print(repo["name"])

aa = {"name": "aviel", "lname": "buskila", "age": 33}
print(aa["age"])
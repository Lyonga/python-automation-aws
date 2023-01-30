import requests

# replace with your own user 
user = "nanuchi"
response = requests.get(f"https://api.github.com/users/{user}/repos")
my_projects = response.json()

# print just the names and urls
for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n")


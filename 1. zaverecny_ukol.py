"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Magdalena Slánská

email: magdalena@slansti.cz

discord: magdalena2586

"""

username = input("enter username:")
password = input("enter password:")

# seznam credentials (username + password)
users = [
    {"name": "bob", "password": "123"},
    {"name": "ann", "password": "pass123"},
    {"name": "mike", "password": "password123"},
    {"name": "liz", "password": "pass123"}
]
authenticated = False
for user in users:
    if ((user["name"] == username) and (user["password"] == password)):
        authenticated = True
        break
print(authenticated, username, password) 

if not authenticated:
    print("unregistered user, terminating the program..")
    quit()

print("Welcome to the app", username)

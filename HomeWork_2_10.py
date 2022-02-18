import json
import base64
from functools import wraps


def registration(*entry):
    with open("login.json", "r") as js_file:
        data = json.load(js_file)
        j = []
        for i in data:
            j.append(i.get("username"))
            # print(j)
        if entry[0] in j:
            print("That username is taken. Try another.")
        else:
            b = entry[1].encode('utf-8')
            encoded = base64.b64encode(b)
            data.append({"username": entry[0], "password": encoded.decode(), 'age': entry[2]})
            with open("login.json", "w") as yaml_:
                json.dump(data, yaml_, indent=4)

registration("Artash", "pass14",25)

def login_dec(file):
    def login(function):
        @wraps(function)
        def decor(*args):
            with open(file, "r") as login_json:
                login_json = json.load(login_json)
                for i in login_json:
                    if i['username'] == args[0]:
                        b = bytes(i['password'], 'utf-8')
                        data = base64.b64decode(b).decode()
                        # print(data)
                        if data == args[1]:
                            result = function(args[0], args[1])
                            return result
        return decor
    return login


@login_dec("login.json")
def input_login(username, password):
    with open("login.json", "r") as js_file:
        data = json.load(js_file)
        for i in data:
            if i['username'] == username:
                print(i)
    return username, password


# username_1 = input("username: ")
# password_1 = input("password: ")
input_login("Artash", "pass14")

import os
import json
from functools import wraps


def identification(func):
    json_file = os.path.join(os.getcwd(), "login.json")
    username = input("enter username")
    password = input("enter the password")

    def funcion(text):
        with open(json_file, "r") as f:
            data = json.load(f)
            for i in data:
                if i['username'] == username and i['password'] == password:
                    print(i)
                    return func(text)
            raise TypeError("identification failed")
    return funcion

@identification
def say_hello(text):
    print(text)


say_hello("say hello")
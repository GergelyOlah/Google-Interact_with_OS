#!/usr/bin/env python3
import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname("localhost")
    return localhost == "127.0.0.1"
def check_connectivity():
    request = requests.get("http://www.google.com")
    response = request.status_code
    return response == 200 # Automatically returns True or False as the evaluation of the statement here, no need to specify it explicitely.

if check_localhost() and check_connectivity():
    print("Network is OK")
else:
    print("ERROR")





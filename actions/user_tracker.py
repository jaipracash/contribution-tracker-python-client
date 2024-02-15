from config import uca_client
import requests
import json
from datetime import date


@uca_client.action
def user_registration(name: str, email: str, dob: str = None, address: str = None, mobile_number: str = None) -> str:
    url = "http://127.0.0.1:8005/user/user_registration"
    body_data = {
        "name": name,
        "dob": dob,
        "email": email,
        "address": address,
        "mobile_number": mobile_number
    }
    response = requests.post(url, json=body_data)
    json_response = response.json()
    print(json_response)

    if response.status_code == 200:
        json_response = response.json()
        return json.dumps(json_response)

    else:
        message = 'registration failed'
        return json.dumps({"status": False, 'message': message})


@uca_client.action
def read_one_user(uesr_id: int) -> str:
    url = "http://127.0.0.1:8005/user/" + str(uesr_id)
    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()
        print(json_response)
        return json.dumps(json_response)
    else:
        message = 'user not found'
        return (json.dumps({"status": False, 'message': message}))


@uca_client.action
def delete_user(user_id: int) -> str:
    url = "http://127.0.0.1:8005/user/" + str(user_id)
    response = requests.delete(url)

    if response.status_code == 200:
        json_response = response.json()
        print(json_response)
        return json.dumps(json_response)

    else:
        message = 'user not found'
        return json.dumps({'status': False, 'message': message})


@uca_client.action
def read_all_users() -> list[list[str]]:
    url = "http://127.0.0.1:8005/user/"
    response = requests.get(url)

    users_list = [['id', 'name', 'dob', 'email', 'address', 'mobile_number']]

    json_response = response.json()
    for user in json_response:
        users_list.append([
            str(user["id"]),
            str(user["name"]),
            user["dob"],
            user["email"],
            user["address"],
            user["mobile_number"]
        ])

    return users_list

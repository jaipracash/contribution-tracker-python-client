import requests
import json
from datetime import date
from uniconnapps import connector

uca_client = connector.UcaClient(
  connector_endpoint="uca://dp-connector-aws-us-east-1.cloud.uniconnapps.com",
  app_id="ad50c966-479c-4dc0-a8ae-c49df2b738c1",
  client_id="3016dc27-a8a6-4d0d-a57b-e36680e765be",
  client_secret="OlMttUbRY3m8p8RtKogMKbvajCPJ4QMQo0FSqIL3cQtAyyxyICLUiaKOg1CFcHu7"
  )


@uca_client.action
def user_registration(name: str,  email: str, dob: str = None, address: str = None, mobile_number: str = None) -> str:
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
def read_one(id: int) -> str:
    url = "http://127.0.0.1:8005/user/"+str(id)
    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()
        print(json_response)
        return json.dumps(json_response)
    else:
        message = 'user not found'
        return (json.dumps({"status": False, 'message': message}))


@uca_client.action
def delete_user(id:int) -> str:
    url = "http://127.0.0.1:8005/user/"+str(id)
    response = requests.delete(url)

    if response.status_code == 200:
        json_response = response.json()
        print(json_response)
        return json.dumps(json_response)

    else:
        message = 'user not found'
        return json.dumps({'status': False, 'message': message})

@uca_client.action
def read_all() -> list[list[str]]:
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








if __name__ == '__main__':
  uca_client.run_forever()
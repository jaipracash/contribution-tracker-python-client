from config import uca_client
import requests
import json


@uca_client.action
def contribution_registation(event_id: int, amount: int, name: str = None, address: str = None, mobile_number: str = None) -> str:
    url = "http://127.0.0.1:8005/contribution/contributions_registration"
    body_data = {
        "event_id": event_id,
        "name": name,
        "address": address,
        "amount": amount,
        "mobile_number": mobile_number
    }
    response = requests.post(url, json=body_data)
    json_response = response.json()
    print(json_response)
    print(response.status_code)
    if response.status_code == 200:
        json_response = response.json()
        return json.dumps(json_response)

    else:
        message = 'registration failed'
        return json.dumps({"status": False, 'message': message})


@uca_client.action
def delete_contribution(contribution_id: int) -> str:
    url = "http://127.0.0.1:8005/contribution/" + str(contribution_id)
    response = requests.delete(url)
    json_response = response.json()
    if response.status_code == 200:
        json_response = response.json()
        return json.dumps(json_response)
    else:
        message = "failed to delete event"
        status_code = response.status_code
        return json.dumps({"status": False, "status code": status_code, "message": message})

@uca_client.action
def read_one_contribution(contribution_id:int) -> str:
    url = "http://127.0.0.1:8005/contribution/" + str(contribution_id)
    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()
        return json.dumps(json_response)
    else:
        message = "failed to read event"
        return json.dumps({"status": False, "message": message})


import requests


@uca_client.action
def read_all_contributions(event_id: str) -> list[list[str]]:
    url = "http://127.0.0.1:8005/contributionread_all/" + str(event_id)
    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()

        contribution_list = [["id", "event_id", "name", "address", "amount", "mobile_number"]]

        for contribution in json_response:
            contribution_list.append([
                str(contribution['id']),
                str(contribution['event_id']),
                contribution['name'],
                contribution['address'],
                str(contribution['amount']),
                contribution['mobile_number']
            ])

        return contribution_list

    return  json.dumps({"status": False, "message": "failed to read contributions"})


@uca_client.action
def contributions_report(event_id: int) -> str:
    url = "http://127.0.0.1:8005/contribution/report/" + str(event_id)
    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()
        return json.dumps(json_response)
    else:
        message = "failed to read event"
        return json.dumps({"status": False, "message": message})

@uca_client.action
def update_contributions_report(contribution_id: int, event_id: int, name: str, address: str, amount: int, mobile_number: int) -> str:
    url = f"http://127.0.0.1:8005/contribution/{contribution_id}"
    body_data = {
        "event_id": event_id,
        "name": name,
        "address": address,
        "amount": amount,
        "mobile_number": str(mobile_number)
    }

    print("Request Body:", body_data)

    response = requests.put(url, json=body_data)
    print("Response:", response)

    if response.status_code == 200:
        json_response = response.json()
        return json.dumps(json_response)
    else:
        message = "Failed to update event"
        return json.dumps({"status": False, "message": message})
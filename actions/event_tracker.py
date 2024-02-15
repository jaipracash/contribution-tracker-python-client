from  config import uca_client
import requests
import json


@uca_client.action
def event_registration(name: str, date: str, location: str, user_id: int) -> str:
    url = "http://127.0.0.1:8005/event/event_registration"
    body_data = {
        "user_id": user_id,
        "name": name,
        "date": date,
        "location": location
    }
    response = requests.post(url, json=body_data)
    json_response = response.json()
    print(json_response)

    if response.status_code == 200:
        return json.dumps(json_response)

    else:
        message = 'registration failed'
        return json.dumps({"status": False, 'message': message})

@uca_client.action
def read_one_event(event_id: int) -> str:
    url = "http://127.0.0.1:8005/event/"+ str(event_id)
    resposne = requests.get(url)

    if resposne.status_code == 200:
        json_response = resposne.json()
        return json.dumps(json_response)
    else:
        message = "failed to read event"
        return json.dumps({"status": False, "message": message})


@uca_client.action
def delete_event(event_id: int) -> str:
    url = "http://127.0.0.1:8005/event/"+ str(event_id)
    response = requests.delete(url)

    if response.status_code == 200:
        json_response = response.json()
        return json.dumps(json_response)
    else:
        message = "failed to delete event"
        return json.dumps({"status": False, "message": message})

@uca_client.action
def read_all_events() -> list[list[str]]:
    url = "http://127.0.0.1:8005/event/"
    response = requests.get(url)
    event_list = [["id", "user_id", "name", "date", "location"]]
    json_response = response.json()

    if response.status_code == 200:
        for event in json_response:
            event_list.append([
                str(event['id']),
                str(event['user_id']),
                event['name'],
                event['date'],
                event['location']
            ])
        return event_list

    else:
        message  = "failed to read events"
        return {'status': False, 'message': message}




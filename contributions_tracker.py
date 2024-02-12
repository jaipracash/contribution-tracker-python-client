import requests
import json
from uniconnapps import connector

uca_client = connector.UcaClient(
  connector_endpoint="uca://dp-connector-aws-us-east-1.cloud.uniconnapps.com",
  app_id="6a64e722-cb91-4155-baf7-57352f9481b3",
  client_id="78db71ea-06d7-41eb-a13e-6c3306a2bdd0",
  client_secret="bvaEl06txnfyiyrxJRtd5z1vmdY213bCvL4tKEUAXssSojYrQ8rJW6XnuhiOakVz"
  )

@uca_client.action
def contribution_registation(event_id: int, amount: int, name: str = None, address:str = None, mobile_number:str = None) -> str:
  url = "http://127.0.0.1:8005/contribution/contributions_registration"
  body_data = {
    "event_id": event_id,
    "name": name,
    "address": address,
    "amount": amount,
    "mobile_number": mobile_number
}
  response = requests.post(url, json= body_data)
  json_response = response.json()
  print(json_response)
  print(response.status_code)
  if response.status_code == 200:
    json_response = response.json()
    return json.dumps(json_response)

  else:
    message = 'registration failed'
    return json.dumps({"status": False, 'message': message})


if __name__ == '__main__':
  uca_client.run_forever()
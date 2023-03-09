import os
import requests

CAMUNDA_TASK_ID = os.environ['CAMUNDA_TASK_ID']
print(CAMUNDA_TASK_ID)
APPLICATION_NAME = os.environ['APPLICATION_NAME']
print(APPLICATION_NAME)

api_url = "http://localhost:8080/engine-rest/process-instance/"+CAMUNDA_TASK_ID+"/variables"
print(api_url);
response = requests.get(api_url)
camunda_response = response.json()
print(camunda_response)


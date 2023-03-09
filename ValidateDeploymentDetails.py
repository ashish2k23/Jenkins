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
print(f"Application name is {camunda_response['applicationname']['value']}")
print(camunda_response['reqstatus']['value'])
if APPLICATION_NAME == camunda_response['applicationname']['value'] && camunda_response['reqstatus']['value'] == 'Approved':
	print("deplyment request is validated")
else:
	print("deplyment request is not validated")
	

print("***************after JSON response END*************** ")
#for key in camunda_response:
   #print(key, '->', camunda_response[key])
   #print(key, '->',camunda_response[key].values())



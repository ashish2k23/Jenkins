import os
import requests

CAMUNDA_TASK_ID = os.environ['CAMUNDA_TASK_ID']
print(f"Camunda task ID from jenkins deployment request is {CAMUNDA_TASK_ID}")
APPLICATION_NAME = os.environ['APPLICATION_NAME']
print(f"Application Name from jenkins deployment request is {APPLICATION_NAME}")
api_url = "http://localhost:8080/engine-rest/process-instance/6ffa931c-c1b4-11ed-a410-005056c00008/variables"
#api_url = "http://localhost:8080/engine-rest/process-instance/"+CAMUNDA_TASK_ID+"/variables"
#api_url = "https://dmn-eai-dev.kdc.logistics.corp/engine-rest/process-instance/"+CAMUNDA_TASK_ID+"/variables"

print(api_url);
response = requests.get(api_url)
camunda_response = response.json()
print(camunda_response)
camunda_response_applicationname = camunda_response.get('applicationname').get('value')
camunda_response_requeststatus = camunda_response.get('reqstatus').get('value')
print(f"Application name is  {camunda_response_applicationname}")
print(f"Deployment status is {camunda_response_requeststatus}")
if(APPLICATION_NAME == camunda_response_applicationname and camunda_response_requeststatus == 'Approved'):
	print("deployment request is validated")
else:
	print("deployment request is not validated")
	

print("***************after JSON response END*************** ")
#for key in camunda_response:
   #print(key, '->', camunda_response[key])
   #print(key, '->',camunda_response[key].values())



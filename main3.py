import json
import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass


if __name__ == "__main__":
    email = input("E-mail itbatera: ")
    pwditbatera = getpass("Password itbatera: ")

    auth = HTTPBasicAuth(email, pwditbatera)
    uri = "https://demo.service-now.com/incident.do?JSONv2"

    headers = {
        "Accept": "application/json;charset=utf-8",
        "Content-Type": "application/json"
    }

    # define payload for request, note we are passing the sysparm_action variable in the body of the request
    payload = {
        "sysparm_action": "insert",
        "category": "Infrastructure",
        "impact": "1",
        "urgency": "2",
        "short_description": "Automated ticket Short Description",
        "description": "Automated ticket Description",
        "cmdb_ci": "Email",
        "caller_id": "Allan Schwantd",
        "contact_type": "Email",
        "company_name": "CMPv2",
    }

    r = requests.post(url=uri, data=json.dumps(payload), auth=auth, verify=False, headers=headers)
    content = r.json()
    assert (r.status_code == 200)
    print ("Response Status Code: " + str(r.status_code))
    print ("Response JSON Content: " + str(content))
import json
import requests

thingworx_url = "https://asnppasjn74.preprod-asn.com:8443/Thingworx/Resources/SourceControlFunctions/Services/ImportSourceControlledEntities"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "AppKey": "03200291-aaa7-435c-b6ba-b0b42cc2548e"
}


payload = {
"repositoryName": "SystemRepository",
"path": "/Test/Test_Project/Things",
"overwritePropertyValues": True
}


try:
    response = requests.post(
        url = thingworx_url, 
        headers = headers, 
        data = json.dumps(payload), 
        verify = False
    )
    
    print("Response Code:", response.status_code)
    print("Response Body:", response.text)
    print(response)
    
except Exception as e:
    print("An error occured:", str(e))
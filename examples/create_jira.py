# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://dailyproject-management.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0e5FN5aJs3Zi_mVNzcVNZTuvD-8HSsdNppiIDrHM-rzwmupDDLKaveTughdm5PWGhTMTIVw823hAJNtd_Wy8unxnWaMpS3M5jsxYt3H_iMmADbP2q-dhAfBZbxDzowBzKt5PMacNMczEvUixfgaRclc53CsoRtabgBe8-GsMJePY=F584F9AE"

auth = HTTPBasicAuth("authenticate007@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
   
    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "First Jira Ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    
    "issuetype": {
      "id": "10007"
    },
   
    "project": {
      "key": "GJA"
    },
   
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
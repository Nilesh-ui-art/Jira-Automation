# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://dailyproject-management.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0uH7FvNLyYkD-MKte6DyJVCCiSvdknp77WW38lC9-0bRppVZKSoHGPY2SRrY7wKRRA5xPFhTqh6fiT-praVyn9GdT2H-43d_UiMtO1wk5rZBY_otV6k7a5U_g-IBHyE-nDyQHcHdZFCn44H1ucLD9KXAJm46XKqaTpreDcS3zftk=A834438A"

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
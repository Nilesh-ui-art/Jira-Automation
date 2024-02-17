from flask import Flask, request
from requests.auth import HTTPBasicAuth
import requests
import json

# Create Flask Application Instance
app = Flask(__name__) 

@app.route("/createJIRA", methods=['POST'])
def createJIRA():
    url = "https://dailyproject-management.atlassian.net/rest/api/3/issue"

    API_TOKEN = "ATATT3xFfGF0RT2iK5GQpyBGTaDM1e9mnPBD96Wnqy3_aMuqyi7Iewefm7J9gv33z2wW-OUW3I0e2eackDla4JAt_Yl2MccSf5RjlwXlB4CqsjVq4TWfAa-y2uSTbMidFfBzHgxTSSf2JsBMcwNAxS7NJgGSGy7poR6MOLdsCAR5a0s-m3NUYPs=FADAB359"

    auth = HTTPBasicAuth("authenticate007@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "Jira Ticket from Repo Jira-Automation",
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
            "summary": "Jira Ticket for Repo Automation"
        },
        "update": {}
    })

    webhook = request.json
    if webhook['comment'].get('body') == "/jira":
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        return 'Jira issue is created if comment includes /jira'

if __name__ == "__main__":
    app.run('0.0.0.0')

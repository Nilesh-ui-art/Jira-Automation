from flask import Flask, request
from requests.auth import HTTPBasicAuth
import requests
import json

# Create Flask Application Instance
app = Flask(__name__) 

@app.route("/createJIRA", methods=['POST'])
def createJIRA():
    url = "https://dailyproject-management.atlassian.net/rest/api/3/issue"

    API_TOKEN = "ATATT3xFfGF0N7-GP_kWK8c1_aUG5WsuQrwAggh8Lt_kZy7Q-oo98zoEESta-xwn9l76EZmJ79qWpG6d0McBBr-snernfDPzcIn4mALXupC1b2roMN7CY4CPb-S6kWit0RAWAoI0WT4bA4aTHBYSVSakyzYGEYMnpvZJ6ecpeAJXUIEU77lLw24=2BC4B139"

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

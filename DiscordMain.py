#!/usr/bin/env python
# coding: utf-8


import json
import requests
import time


# Set Discord webhook

webhook_url = '[PASTE HERE]'
discord_data = {'content': 'Your daily spam :eyes: (10 sec interval)'}


while True:
    response = requests.post(
        webhook_url, data = json.dumps(discord_data),
        headers = {'Content-Type': 'application/json'}
    )
    
    if response.status_code != 204:
        raise ValueError(
            'Request to Discord returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
    time.sleep(10)




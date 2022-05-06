

import os, requests, uuid, json

key_var_name = '<SECRET KEY found in azure documentation>'

resource_key = key_var_name

region_var_name = 'eastus'

region = region_var_name

endpoint_var_name = '<ENDPOINT found in azure documentation>'

endpoint = endpoint_var_name

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
path = '/translate?api-version=3.0'
params = '&from=en&to=de&to=it'
constructed_url = endpoint + path + params

headers = {
    'Ocp-Apim-Subscription-Key': resource_key,
    'Ocp-Apim-Subscription-Region': region,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text' : 'Hello World!'
}]
request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))
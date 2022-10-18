import os
from cloudmesh.common.Shell import Shell
import json
import requests

n = 100
for provider in ['aws', 'google']:
    for i in range(n):
        r=requests.get(f'http://localhost:8000/translate/cat?provider=ibm&fromlang=en&tolang=de')
        r=r.splitlines()[:-1]
        r=" ".join(r)
        d = eval(r)
        print(f"{d['time']}, {d['provider']}, {d['output']}, requests")

        
    


import os
from cloudmesh.common.Shell import Shell
import json

n = 100
for provider in ['aws', 'google']:
    for i in range(n):
        r=Shell.run(f'cms nlp translate --provider={provider} --from=de --to=en --region=us-east-1 hallo welt').strip()
        r=r.splitlines()[:-1]
        r=" ".join(r)
        d = eval(r)
        print(f"{d['time']}, {d['provider']}, {d['output']}")

        
    


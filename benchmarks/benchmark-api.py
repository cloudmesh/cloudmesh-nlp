import os
from cloudmesh.common.Shell import Shell
from cloudmesh.nlp.provider import Translate
import json

n = 100

for provider in ['aws', 'google', 'ibm']:
    translator = Translate(provider=provider)
    for i in range(n):
        result = translator.get(content='hallo welt', SourceLanguageCode='de', TargetLanguageCode='en')
        # r=Shell.run(f'cms nlp translate --provider={provider} --from=de --to=en --region=us-east-1 hallo welt').strip()
        # r=r.splitlines()[:-1]
        # r=" ".join(r)
        d = eval(result)
        print(f"{d['time']}, {d['provider']}, {d['output']}, api")

        
    


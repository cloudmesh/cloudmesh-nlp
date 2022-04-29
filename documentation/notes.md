## google 

output:

```
{
    'translatedText':         'Hello World',
    'detectedSourceLanguage': 'de',
    'input':                  'hallo welt'
}
```

here 
similarites
differences


## aws

output:

```
{
    'TranslatedText':     'hello world',
    'SourceLanguageCode': 'de',
    'TargetLanguageCode': 'en',
    'ResponseMetadata': {
        'RequestId': 'e26c352e-7a8c-40ea-85e3-c216de42f8fe',
        'HTTPStatusCode': 200, 
        'HTTPHeaders': {
            'x-amzn-requestid': 'e26c352e-7a8c-40ea-85e3-c216de42f8fe',
            'cache-control': 'no-cache',
            'content-type': 'application/x-amz-json-1.1',
            'content-length': '84',
            'date': 'Fri, 29 Apr 2022 20:33:51 GMT'
        },
        'RetryAttempts': 0
    }
}
```
here
similarites
differences

## hybrid nlp cloud-service output specification

based on our comparison suggest the following output:

{
    'input':          'Hello World'
    'input_language':  'en'
    'output_language': 'de'
    'dutput':          'Hallo Welt'
    'date':            'Fri, 29 Apr 2022 20:33:51 GMT'

}

We have these feilds for this reason:

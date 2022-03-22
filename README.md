# Documentation

## Abstract


## Installation for developers with ssh access

First activate your key

```
eval `ssh-agent`
ssh-add
```

Now install cloudmesh-nlp from source.

``` 
cd
mkdir ~/cm
cd cm
where py
py.exe --version
py.exe -m venv ~/ENV3
source ~/ENV3/Scripts/activate
pip install pip -U
pip install cloudmesh-installer
cloudmesh-installer --ssh get catalog
cms help
git clone git@github.com:laszewsk/nist.git
git clone git@github.com:cloudmesh/cloudmesh-nlp.git
cd cloudmesh-nlp
pip install -e . (edited) 
```

## Survey of NLP service

The next sections only relate t our servey a sruvery and do not belong to the nlp code

### textanalysis-text-summarization.p.mashape.com

GvL: As far as i can tell this service is dead?

Myles: can you comment, i think you added it?

#### First: must install unirest

only works in python 2.7 and this project is no longer active, use python requests instead.

TODO: fix this code while using python request

```
pip install unirest

import unirest
```

#### second: previous json request
(can have any url implemented)

```
{
    "url": "http://en.wikipedia.org/wiki/Automatic_summarization",
    "text": "",
    "sentnum": 8
}
```

#### third: post request
(can have any url implemented)

```
response = unirest.post("https://textanalysis-text-summarization.p.mashape.com/text-summarizer",
    headers={
        "X-Mashape-Authorization": "Mashape API Key",
        "Content-Type": "application/json"
    },
    params="{\"url\":\"http:\/\/en.wikipedia.org\/wiki\/Automatic_summarization\",\"text\":\"\",\"sentnum\":8}"
);
```

#### fourth: the api key to operate:

```
import unirest
response = unirest.post("https://textanalysis-text-summarization.p.mashape.com/text-summarizer",
     headers={
         "X-Mashape-Authorization": "Your Mashape API Key",
         "Content-Type": "application/json"
     },
     params="{\"url\":\"http:\/\/en.wikipedia.org\/wiki\/Automatic_summarization\",\"text\":\"\",\"sentnum\":8}"
 );
 dir(response)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_body', '_code', '_headers', '_raw_body', 'body', 'code', 'headers', 'raw_body']
 response.code
200
 response.headers

   response.body
{u'sentences': [u'Document summarization is another.', u'Generally, there are two approaches to automatic summarization: extraction and abstraction.', u'Furthermore, evaluation of extracted summaries can be automated, since it is essentially a classification task.', u'Even though automating abstractive summarization is the goal of summarization research, most practical systems are based on some form of extractive summarization.', u'Extractive methods work by selecting a subset of existing words, phrases, or sentences in the original text to form the summary.', u'The state-of-the-art abstractive methods are still quite weak, so most research has focused on extractive methods.', u'These systems are known as multi-document summarization systems.', u'People are subjective, and different authors would choose different sentences.']}
    response.raw_body
'{\n  "sentences": [\n    "Document summarization is another.",\n    "Generally, there are two approaches to automatic summarization: extraction and abstraction.",\n    "Furthermore, evaluation of extracted summaries can be automated, since it is essentially a classification task.",\n    "Even though automating abstractive summarization is the goal of summarization research, most practical systems are based on some form of extractive summarization.",\n    "Extractive methods work by selecting a subset of existing words, phrases, or sentences in the original text to form the summary.",\n    "The state-of-the-art abstractive methods are still quite weak, so most research has focused on extractive methods.",\n    "These systems are known as multi-document summarization systems.",\n    "People are subjective, and different authors would choose different sentences."\n  ]\n}'
```
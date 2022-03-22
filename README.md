# Documentation

## Abstract


## Instalation for developers with ssh access

```
eval `ssh-agent`
ssh-add
```

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






## Python 2.7 (experimental and not part of cloudmesh-nlp)

This should not be used, but is an experiment for Python 2.7 while looking into an old implementation called unirest.

A link here is missing so no one realy knows what it is ;-)

Apparentl it is supposed to be a text summeraziation api for python

to mimmic:

### First: must install unirest

pip install unirest

import unirest

### second: previous json request
(can have any url implemented)

{
    "url": "http://en.wikipedia.org/wiki/Automatic_summarization",
    "text": "",
    "sentnum": 8
}

### third: post request
(can have any url implemented)


response = unirest.post("https://textanalysis-text-summarization.p.mashape.com/text-summarizer",
    headers={
        "X-Mashape-Authorization": "Mashape API Key",
        "Content-Type": "application/json"
    },
    params="{\"url\":\"http:\/\/en.wikipedia.org\/wiki\/Automatic_summarization\",\"text\":\"\",\"sentnum\":8}"
);


### fourth: the api key to operate:

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

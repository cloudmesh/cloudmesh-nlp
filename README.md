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

## Amazon Comphrend

Amazon comphrehend is a cloud service that identifies key meanings and relationships. These entities can be pulled from a social media post, customer support ticket, news feeds, etc.

purpose: amazon comphrend cuts the time to pick key information from text. greatly reducing the amount of time for analysis.

Amazon models are easily trainable and will adapt entity findings to become part-codes or other key peieces of info that make sense for your business.

Difference bewteen other serices like ibm watson:

Amazon comphrend is really good at picking out information while IBM Watson is good at taking that information and answering questions.

to get started using amazon comprehend check out: https://github.com/aws-samples/aws-nlp-workshop/tree/master/3_GenderClassification


## IBM Watson

IBM Watson is a service produced by IBM that uses deep learning to extract meaning from text. These meanings can answer consumer questions with automation, or help in other customer service businesses.

purpose: extract key entities such as, catagories, classifications, entities, keywords etc. this service then takes those key words and uses your business adapted machine learning model to answer specific questions about that text.

These models are highly adaptable to the use of your business and vary between text recognition.

to get started using amazon watson check out: https://www.ibm.com/cloud/watson-natural-language-understanding


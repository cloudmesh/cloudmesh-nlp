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

Amazon comphrehend is a cloud service that identifies key meanings and relationships. These entities can be pulled from
a social media post, customer support ticket, news feeds, etc.

purpose: amazon comphrend cuts the time to pick key information from text. greatly reducing the amount of time for
analysis.

Amazon models are easily trainable and will adapt entity findings to become part-codes or other key peieces of info 
that make sense for your business.

Difference between other services like ibm watson:

Amazon comphrend is really good at picking out information while IBM Watson is good at taking that information and 
answering questions.

to get started using amazon comprehend check out:
<https://github.com/aws-samples/aws-nlp-workshop/tree/master/3_GenderClassification>


## IBM Watson

IBM Watson is a service produced by IBM that uses deep learning to extract meaning from text. These meanings can answer 
consumer questions with automation, or help in other customer service businesses.

purpose: extract key entities such as, categories, classifications, entities, keywords etc. this service then takes 
those keywords and uses your business adapted machine learning model to answer specific questions about that text.

These models are highly adaptable to the use of your business and vary between text recognition.

to get started using amazon watson check out: <https://www.ibm.com/cloud/watson-natural-language-understanding>

## Microsoft Azure

Azure Cognitive Services are cloud-based services that help you build cognitive intelligence into your applications. 
Cognitive services are categorized in speech, vision , language and decision.

purpose: For language it has a feature that uses NLU so that interactions with bots, apps and IoT devices can be build 
up.

Text analytics helps  gain insights from unstructured texts using NLP. It also includes collection of features such as 
sentiment analysis, key phrase extraction, language detection and named entity detection.

you can get started check out: <https://azure.microsoft.com/en-in/services/cognitive-services/>

## Google

Google has Natural Language client libraries and Language operators which help to use Cloud Natural Language API. 
Language Operators work via Apache Airflow

purpose: reveal the structure and meaning of text via powerful machine learning models. can be used to extract 
information about people, places, events.

This can be used to understand sentiments about your product on social media. It can also be used cases for Analyzing 
Entities, Analyzing Entity Sentiment, Analyzing Sentiment, Classifying Content

to get started 

you can get started check out: <https://airflow.apache.org/docs/apache-airflow-providers-google/stable/index.html>
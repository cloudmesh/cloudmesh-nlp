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
Cognitive services are categorized in speech, vision, language and decision.

Language service uses NLU so that interactions with bots, apps and IoT devices can be build up.

Text analytics helps gain insights from unstructured texts using NLP. It also includes collection of features such as 
sentiment analysis, key phrase extraction, language detection and named entity detection.

More information can be found at: <https://azure.microsoft.com/en-in/services/cognitive-services/>

## Sweety Content

1.	MICROSOFT AZURE COGNITIVE SERVICES

Service	                           Description
Text Analytics It helps to gain insights from unstructured text using NLP . 
Sentiment Analysis, Key phrase extraction, Language detection and Named Entity Detection
Speech CLI 	Speech recognition, Speech Synthesis, Speech Translation
Language Understanding	A feature of Cognitive Service for Language that uses natural language understanding (NLU) so 
people can interact with your apps, bots, and IoT devices.
Quickly build a custom, multilingual solution
 | Service              |                     Description                                                             |
 |:--------:            | :------------------------------------------------:                                          |
 |Text Analytics        |It helps to gain insights from unstructured text using NLP.                                  |
 |                      |Sentiment Analysis, Key phrase extraction, Language detection and                            |
 |                      |Named Entity Detection.                                                                      |
 |Speech CLI            |Speech recognition, Speech Synthesis, Speech Translation                                     |
 |Language Understanding|A feature of Cognitive Service for Language that uses natural language understanding (NLU) so| 
 |                      |people can interact with your apps, bots, and IoT devices.                                   |
 |                      |Quickly build a custom, multilingual solution                                                |

2.	Google Cloud Natural Language

The Cloud Natural Language API provides natural language understanding technologies to developers, including sentiment 
analysis, entity analysis, entity sentiment analysis, content classification, and syntax analysis

•	Sentiment analysis inspects the given text and identifies the prevailing emotional opinion within the text.
•	Entity analysis inspects the given text for known entities and returns information about those entities. 
•	Entity sentiment analysis inspects the given text for known entities, returns information about those entities, 
    and identifies the prevailing emotional opinion of the entity within the text.
•	Syntactic analysis extracts linguistic information, breaking up the given text into a series of sentences and tokens
    providing further analysis on those tokens.
•	Content classification analyses text content and returns a content category for the content.

  



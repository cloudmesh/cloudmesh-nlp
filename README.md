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
social media posts, customer support tickets, news feeds, etc.
TODO: What is etc?


Amazon comphrend intents to cuts the time to pick key information from text, and intents to reduces the amount of time 
for the analysis.


Amazon models are easily trainable and will adapt entity findings to become part-codes or other key peieces of info 
that make sense for your business.

Difference between other services like ibm watson:

Amazon comphrend is really good at picking out information while IBM Watson is good at taking that information and 
answering questions.

to get started using amazon comprehend check out:
<https://github.com/aws-samples/aws-nlp-workshop/tree/master/3_GenderClassification>


| Amazon Comphrehend |   Yes    | No  |
| ------------- |:-------------:| -----:|
| Account creation required under AWS cloudservices  | - [x] |  |
| Ease of use | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

- [ ] (for unchecked checkbox)
- [x] (for checked checkbox)
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


## Google

Google has Natural Language client libraries and Language operators. The Language Operators can be used via Apache 
Airflow.
TODO: are language operators always needed to access apache airflow?
Google offers a Cloud Natural Language API.
TODO: What does it offer?

The purpose of Natural Language is to reveal the structure and meaning of text via powerful machine learning models.
Language operators can be used to extract information about people, places, events.

Language operators can be used to understand sentiments about your product on social media. It can also be used 
for Analyzing 
Entities, Analyzing Entity Sentiment, Analyzing Sentiment, Classifying Content

More information can be found at: <https://airflow.apache.org/docs/apache-airflow-providers-google/stable/index.html>




## Microsoft azure cognitive services


| Service              |                                          Description                                          |
|:--------:            |:---------------------------------------------------------------------------------------------:|
|Text Analytics        |                  It helps to gain insights from unstructured text using NLP.                  |
|                      |               Sentiment Analysis, Key phrase extraction, Language detection and               |
|                      |                                    Named Entity Detection.                                    |
|Speech CLI            |                   Speech recognition, Speech Synthesis, Speech Translation                    |
|Language Understanding| A feature of Cognitive Service for Language that uses natural language understanding (NLU) so | 
|                      |                  people can interact with your apps, bots, and IoT devices.                   |
|                      |                         Quickly build a custom, multilingual solution                         |


## Google Cloud Natural Language

The Cloud Natural Language API provides natural language understanding technologies to developers, including sentiment 
analysis, entity analysis, entity sentiment analysis, content classification, and syntax analysis

* Sentiment analysis inspects the given text and identifies the prevailing emotional opinion within the text.
* Entity analysis inspects the given text for known entities and returns information about those entities. 
* Entity sentiment analysis inspects the given text for known entities, returns information about those entities, 
  and identifies the prevailing emotional opinion of the entity within the text.
* Syntactic analysis extracts linguistic information, breaking up the given text into a series of sentences and tokens
  providing further analysis on those tokens.
* Content classification analyses text content and returns a content category for the content.

  



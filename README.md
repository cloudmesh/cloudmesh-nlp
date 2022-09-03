# Documentation

## Content

* Abstarct
* Survey of ....
  * subsection

## Abstract

TODO: THIS ABSTRACT DOES NOT REFLECT WHAT THIS PROJECT IS ABOUT.

Natural Language operators are everywhere in technology.  They aim to
relate machine learning and human needs for the better good of a
business practice or information system. Some of these systems are
operated by large cloud providers such as Google, I BM Watson and
Amazon. The goal of this study is to highlight what services these
cloud providers offer. Another goal of this study was taking what
these operators can do considering machine limitations, and
implementing those services into a catalog called cloudmesh.  This
catalog would then be able for reuse for data scientists, information
analysts, and other researchers. The design of this study was to take
a deeper look into the composition of language translation,
Text-Entity comprehension, and language conversion. Cloud providers in
modern day were our main focus, ex. Google, IBM, Amazon, and Microsoft
Azure. Our findings have been minimal, however, they highlight the
larger ability to use these services in other forms of
reproduction. Subsequently, starting a conversation for how these
services can benefit common business practices is a very important
subject in our research and should be continued past the initial
research stages.


## Contents

1. Installation
2. Amazon comphrend 
  - description
  - Amazon comphrend quickstart steps.
3. IBM Watson Natural language 
  - IBM watson natural language description
  - quickstart for IBM watson natural language
4. Google Translation 
  - Google Natural Language description
  - How to get started.


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
python.10 --version
python3.10 -m venv ~/ENV3
source ~/ENV3/Scripts/activate
pip install pip -U
pip install cloudmesh-installer
cloudmesh-installer --ssh get catalog
cms help
git clone git@github.com:laszewsk/nist.git
git clone git@github.com:cloudmesh/cloudmesh-nlp.git
cd cloudmesh-nlp
pip install -e .
```

## Survey of NLP service

The next sections only relate t our servey a sruvery and do not belong
to the nlp code

## NLP Services on Amazon

Which services exists write paragraph

### Amazon Comphrend

Amazon comphrehend is a cloud service that identifies key meanings and
relationships. These entities can be pulled from social media posts,
customer support tickets, news feeds, media outlets, televison
scripts.  Amazon comphrend intents to cuts the time to pick key
information from text, and intents to reduces the amount of time for
the analysis.  Amazon models are easily trainable and will adapt
entity findings to become part-codes or other key peieces of info that
make sense for your business.

Difference between other services like ibm watson: Amazon comphrend is
really good at picking out information while IBM Watson is good at
taking that information and answering questions.  to get started using
amazon comprehend check out:
<https://github.com/aws-samples/aws-nlp-workshop/tree/master/3_GenderClassification>


| Amazon Comphrehend                                |   Yes    |   No |
|---------------------------------------------------|:-------------:|----:|
| Account creation required under AWS cloudservices | [x] |     |
| billing required?                                 |   [x]   |     |
| Region required?                                  | [x]      |     |



## NLP Services on IBM Watson

Which services exists write paragraph

if watson has multiple services each should get its own subsection


IBM Watson is a service produced by IBM that uses deep learning to
extract meaning from text. These meanings can answer consumer
questions with automation, or help in other customer service
businesses.

 This is not a ppt:


purpose: extract key entities such as, categories, classifications,
entities, keywords etc. this service then takes those keywords and
uses your business adapted machine learning model to answer specific
questions about that text.  These models are highly adaptable to the
use of your business and vary between text recognition.

To get started using amazon watson check out:
<https://www.ibm.com/cloud/watson-natural-language-understanding>

## NLP Services on  Microsoft Azure

Which services exists write paragraph

each should get its own subsection


### Microsoft Azure Cognitive Services

Azure Cognitive Services are cloud-based services that help you build
cognitive intelligence into your applications.  Cognitive services are
categorized in speech, vision, language and decision.  Language
service uses NLU so that interactions with bots, apps and IoT devices
can be build up.  Text analytics helps gain insights from unstructured
texts using NLP. It also includes collection of features such as
sentiment analysis, key phrase extraction, language detection and
named entity detection.

More information can be found at:
<https://azure.microsoft.com/en-in/services/cognitive-services/>



## Google

Google has Natural Language client libraries and Language
operators. The Language Operators can be used via Apache Airflow.
Google offers a Cloud Natural Language API.  The purpose of Natural
Language is to reveal the structure and meaning of text via powerful
machine learning models.  Language operators can be used to extract
information about people, places, events.  Language operators can be
used to understand sentiments about your product on social media. It
can also be used for Analyzing Entities, Analyzing Entity Sentiment,
Analyzing Sentiment, Classifying Content

More information can be found at:
<https://airflow.apache.org/docs/apache-airflow-providers-google/stable/index.html>



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



## NLP services on Google


The Cloud Natural Language API provides natural language understanding
technologies to developers, including sentiment analysis, entity
analysis, entity sentiment analysis, content classification, and
syntax analysis.

* Sentiment analysis inspects the given text and identifies the
  prevailing emotional opinion within the text.

* Entity analysis inspects the given text for known entities and
  returns information about those entities.

* Entity sentiment analysis inspects the given text for known
  entities, returns information about those entities, and identifies
  the prevailing emotional opinion of the entity within the text.

* Syntactic analysis extracts linguistic information, breaking up the
  given text into a series of sentences and tokens providing further
  analysis on those tokens.

* Content classification analyses text content and returns a content
  category for the content.

<<<<<<< HEAD
* Transaltion service

### Authentication and AUthorization

Explain how you can acess this service (possibly api key and how to use them in your prg. PLEASE DO NEVER POST OR INCLUDE YOUR API KE IN A CLOUMESH DIR.)

filename of the google_api_key

```
mkdir ~/.cloudmesh/nlp
cp  google_api_key ~/.cloudmesh/nlp/.
```
Now you can use with 

```python
from cloudmesh.common.util import readfile

api_key = readfile("~/cloudmesh/nlp/google_api_key")
```

### Translation service

can you get it to run?

* Documentation: <https://cloud.google.com/translate/docs>
* Example: <https://github.com/googleapis/python-translate/blob/HEAD/samples/snippets/snippets.py>

### Sentiment analysis 

details

### Entity analysis inspects

details

### Entity sentiment analysis

details 

### Syntactic analysis

details

## Content classification 

details

### Cloud Natural Language API


Google has Natural Language client libraries and Language
operators. The Language Operators can be used via Apache Airflow.

Google offers a Cloud Natural Language API.

The purpose of Natural Language is to reveal the structure and meaning
of text via powerful machine learning models.  Language operators can
be used to extract information about people, places, events.

Language operators can be used to understand sentiments about your
product on social media. It can also be used for Analyzing Entities,
Analyzing Entity Sentiment, Analyzing Sentiment, Classifying Content

link  missing



### Google Cloud Natural Language


=======
## Fast api 

### to start using fast api

<http://127.0.0.1:8000/translate/hello?fromlang=en&tolang=fr&provider=google>
 

### steps to get started with google translate:

1. To get started making a translation service using google. first,
   you must sign up for a free trial of google cloud here:
   https://cloud.google.com/free?_ga=2.146308663.-2078371114.1649107776

2. Once an account is set up with billing you now have a $300 free
   credit from google to use and test a multitude of service they
   provide. The next step is to create a project. On your dashboard
   you now need to create a new project.

3. After creating a new project you want to enable an api key for
   google cloud translation. On your dashboard you will click on apis on
   the left tab.

4. Create new Cloud Natural Language api (This will be under machine
   learning).

5. If billing is enabled you will now have a api in use for your
   project.
  
6. You now must make credentials for that api. Click the create
   credentials tab at the top of your activated api page. In order to
   create an client id you must do this step. Creating credentials is
   fairly simple, it involves adding an email to set the project
   owner. Any Users for the project will be able to contact you
   through your credentials you provide. Next you will be given a
   client Id (Hold on to this).

7. A good step now is to start using and test using the Activated
   Cloud Translation api.

8. you can install the client libraries to test some of the
   pre-existing examples for language translation Google offers.

    ```
    pip install -r requirements.txt
    ```

    or

    ```
    pip install -e .
    ```

    Now, you must import the cloud translation api client you will use
    this script in most examples and in Google's basic language
    programming.

    ```
    from google.cloud import translate_v2
    ```

9. Google offers a large variety of services and abilitys to alter
   language translation, Time to get started!





curl -X 'GET' \
  'http://localhost:8000/translate/hello?provider=google&fromlang=en&tolang=de' \
  -H 'accept: application/json'




docs 
redocs


aws documentation
papermd
fast api update

## Acknowledgments

Work conducted to publish this activity was funded by the NSF
CyberTraining: CIC: CyberTraining for Students and Technologies
from Generation Z with the awadrd numbers 1829704 and 2200409.

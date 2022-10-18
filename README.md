# Documentation

## Content

* Abstarct
* Survey of ....
  * subsection

## Abstract

Natural Language processing is an imprtant application in todays ever more conected world.
Many cloud providers offer oline services related to natural language processing.
Our goal is to demonstrate a multicloud analytics service, that can utilize mutiple such 
services and on demand switch between them in order to return a result. We focus on language 
translation from AWS, Azure, Google and IBM. Other providers and additional services could 
easily be integrated while using the language translation service as an example.
We compare the time and cost for a number of translations in order to identify a 
scheduling service that based on user specifiable selection criteria. 

TODO: To integrate in future other services, we also provide a service catalog that 
can be used to select aother then translation services. Through this catalog service 
selection will be simplified.



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

### Windows

```bash
cd
mkdir ~/cm
cd cm
where py
python3 --version
python3 -m venv ~/ENV3
source ~/ENV3/Scripts/activate
pip install pip -U
pip install cloudmesh-installer
cloudmesh-installer --ssh get nlp
cms help
# git clone git@github.com:laszewsk/nist.git
```

### macOS or Linux

```bash
cd
mkdir ~/cm
cd cm
where py
python --version
python -m venv ~/ENV3
source ~/ENV3/bin/activate
pip install pip -U
pip install cloudmesh-installer
cloudmesh-installer --ssh get nlp
cms help
# git clone git@github.com:laszewsk/nist.git
```

## Survey of NLP service

The next sections only relate t our servey a sruvery and do not belong
to the nlp code

## NLP Services on Amazon

Which services exists write paragraph

### Amazon Comprehend

Amazon comprehend is a cloud service that identifies key meanings and
relationships. These entities can be pulled from social media posts,
customer support tickets, news feeds, media outlets, television
scripts.  Amazon comprehend intents to cuts the time to pick key
information from text, and intents to reduces the amount of time for
the analysis.  Amazon models are easily trainable and will adapt
entity findings to become part-codes or other key pieces of info that
make sense for your business.

Difference between other services like ibm watson: Amazon comprehend is
really good at picking out information while IBM Watson is good at
taking that information and answering questions.  to get started using
amazon comprehend check out:
<https://github.com/aws-samples/aws-nlp-workshop/tree/master/3_GenderClassification>


| Features                                       | AWS Comprehend  | IBM Watson |
|------------------------------------------------|:---------------:|:----------:|
| Account creation required under cloud provider |       Yes       |            |
| Billing required?                              |       Yes       |            |
| Region required?                               |       Yes       |            |



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

<http://127.0.0.1:8000/translate/hello?fromlang=en&tolang=fr&provider=google> 

## Google Translate Quickstart

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
   credentials tab at the top of your activated api page. Click
   Service account and enter a memorable account ID such as cloudmesh.
   Then click Create and Continue, and then Done. Click on the Service
   Account at the bottom, click Keys, Add key, Create new key, JSON,
   and then Create.

7. After downloading the JSON file, move it to the ~/.cloudmesh/nlp
   folder as cloudmesh.json:

```bash
mkdir ~/.cloudmesh/nlp
# replace the command with where you downloaded the json to
mv fantastic-walrus-863440-4b34c5a5ba4.json ~/.cloudmesh/nlp/cloudmesh.json 
```

8. A good step now is to start using and test using the Activated
   Cloud Translation api.

9. You can install the client libraries to test some of the
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

10. Google offers a large variety of services and abilitys to alter
    language translation, Time to get started!

```bash
curl -X 'GET' \
  'http://localhost:8000/translate/hello?provider=google&fromlang=en&tolang=de' \
  -H 'accept: application/json'
```

## AWS Quickstart

1. Create a free AWS account at
https://portal.aws.amazon.com/billing/signup#/

2. Create an IAM user at <https://console.aws.amazon.com/iam/>
by clicking on Users on the left hand side and clicking Add users

3. Specify any user name (for example, cloudmesh) and choose the
Access key credential type. Then, click Next: Permissions

4. Click Attach existing policies directly and search for the
`translate` policy using the Search box. Click the check box next
to TranslateFullAccess and click Next: Tags

5. Click Next: Review and then click Create user

6. In terminal, say 
```bash
nano ~/.aws/credentials 
```

Paste in the following template and edit
accordingly, replacing the keys with the
keys found on the page of the AWS user
you just created.

```text
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

Then save the file. Restart FastAPI nlp
server and try out the command:

```bash
curl -X 'GET' \
  'http://localhost:8000/translate/cat?provider=aws&fromlang=en&tolang=de' \
  -H 'accept: application/json'
```

## IBM Watson

1. Register for a free account at
<https://cloud.ibm.com/registration>

2. Create a Language Translator resource
at <https://cloud.ibm.com/catalog/services/language-translator>
by choosing a location from the drop-down closest to your
physical location, check the box on the right side, and click Create

3. Click Manage on left-hand side and, under Credentials, click Download

4. Move the env file that was just downloaded to the ~/.cloudmesh/nlp
directory:

```bash
mkdir ~/.cloudmesh/nlp
# replace the command with where you downloaded the json to
mv ~/Downloads/ibm-credentials.env ~/.cloudmesh/nlp/ibm-credentials.env 
```

5. Test with

```bash
curl -X 'GET' \
  'http://localhost:8000/translate/cat?provider=ibm&fromlang=en&tolang=de' \
  -H 'accept: application/json'
```

docs 
redocs


aws documentation
papermd
fast api update

## Acknowledgments

Work conducted to publish this activity was funded by the NSF
CyberTraining: CIC: CyberTraining for Students and Technologies
from Generation Z with the awadrd numbers 1829704 and 2200409.

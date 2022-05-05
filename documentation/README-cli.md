# Implementation of A Hybrid Cloud natural  Language Example

## How to Implement using Command Line Interface and The Cloudmesh Catalog (AWS Provider)



Step 1: Use the cloudmesh catalog to start the natural language example. [AWS Natural Language Example](/Users/mysol/cm/cloudmesh-nlp/cloudmesh/nlp/provider/aws/translate.py)

Here you will install the catalog first.

On mac

```commandline
python3.10 -m venv ~/ENV3
source ~/ENV3/bin/activate
mkdir cm
cd cm
pip install cloudmesh-installer
cloudmesh-installer -ssh install catalog
```

From here you will install the source packages for this command line reference:
```commandline
pip install -r requirements.txt
```

```commandline
cms help
cms nlp translate --provider=aws --from=en --to=de --region=eu-west-1 hello world
```

The output to this command should look like:
```
{'date': '05/02/2022 14:45:45',
 'input': 'hello world',
 'input_language': 'en',
 'output': 'hallo welt',
 'output_language': 'de',
 'provider': 'aws',
 'time': 0.2641}
Timer: 0.3864s Load: 0.0004s nlp translate --provider=aws --from=en --to=de --region=eu-west-1 hello world
```



-----


## How to Implement using Command Line Interface and The Cloudmesh Catalog (Google Provider)

Step 1: Use the cloudmesh catalog to start the Natural Language example.
[Google Natural Language Example](/Users/mysol/cm/cloudmesh-nlp/cloudmesh/nlp/provider/google/translate.py)

Here you will install the catalog first.

On mac

```commandline
python3.10 -m venv ~/ENV3
source ~/ENV3/bin/activate
mkdir cm
cd cm
pip install cloudmesh-installer
cloudmesh-installer -ssh install catalog
```

From here you will install the source packages for this command line reference:
```commandline
pip install -r requirements.txt
```

```commandline
cms help
cms nlp translate --provider=google --from=en --to=de --region=eu-west-1 hello world
```

The output to this command should look like:
```
{'date': '05/02/2022 14:45:45',
 'input': 'hello world',
 'input_language': 'en',
 'output': 'Hallo Welt',
 'output_language': 'de',
 'provider': 'aws',
 'time': 0.2641}
Timer: 0.3864s Load: 0.0004s nlp translate --provider=aws --from=en --to=de --region=eu-west-1 hello world
```

## heterogenous cloudmesh nlp service


In this documentation we have an example of using a natural language operator from different providers.
This is a service that is started with cloudmesh catalog. After installation of the catalog
there are a list of services that can be used. 
Using ```cms help``` on the command line will give that list of services
this output will look like:
```
Documented commands (type help <topic>):
========================================
EOF      commands  dryrun  host       nlp    quit   stopwatch  var    
banner   config    echo    info       pause  set    sys        version
catalog  debug     gui     inventory  py     shell  sysinfo  
clear    default   help    man        q      sleep  term     
```

Here there is a newly implemented ``nlp`` command. 
This can be accessed by ``cms nlp`` in the command line.
the source code can be found [here](/Users/mysol/cm/cloudmesh-nlp/cloudmesh/nlp/command/nlp.py)

In order to start the translate service from CMS there are a
few arguments we will be using.
cms nlp translate takes the arguments:
```
--provider=google
--from=en
--to=de
--region=eu-west-1
```
The provider is interchangeable from the implemented services 'aws', 'google'
and 'azure'.
The argument ``from`` takes an interchangeable language code offered from the
cloud-providers. This is the language your initial text is decoded in.
The argument ``to`` is the target language the text will be translated to. 
This argument also takes a language code offered from the cloud providers.
A list of Language codes are found here:


| Provider                |          Google          |           aws            |
|-------------------------|:------------------------:|:------------------------:|
| Language	               | Supported Language Codes | Supported Language Codes |
| Afrikaans	              |          af-ZA	          |          af-ZA           |
| Arabic, Gulf            |          	ar-AE          |          	ar-AE       |   
 Arabic, Modern Standard |         	ar-SA	          |          ar-SA       |    
 Chinese, Simplified	    |          zh-CN           |          zh-CN     |      
 Chinese, Traditional    |         	zh-TW	          |          zh-TW         |  
 Danish	                 |          da-DK	          |          da-DK        |   
 Dutch	                  |          nl-NL	          |          nl-NL        |   
 English, Australian	    |          en-AU	          |          en-AU     |      
 English, British	       |          en-GB	          |          en-GB         |  
 English, Indian	        |          en-IN	          |          en-IN	   |       
 English, Irish	         |          en-IE	          |          en-IE	      |    
 English, New Zealand	   |          en-NZ	          |          en-NZ        |   
 English, Scottish	      |          en-AB	          |          en-US        |   
 English, South African  |         	en-ZA	          |          en-ZA       |    
 English, US	            |          en-US	          |          en-US   |        
 English, Welsh	         |          en-WL	          |          en-WL	    |      
 French	                 |          fr-FR           |          fr-FR        |   
 French, Canadian	       |          fr-CA	          |          fr-CA     |      
 Farsi	                  |          fa-IR	          | fa-IR|
 German	                 |        de-DE	            |de-DE|
 German, Swiss	          |          de-CH	          |de-CH|
 Hebrew	         |          he-IL	          |        he-IL|
 Hindi, Indian	          |          hi-IN	          |hi-IN|
 Indonesian	             |          id-ID	          |id-ID|
 Italian 	               |          it-IT           | it-IT |
 Japanese	               |          ja-JP	          | ja-JP	  |
 Korean  	               |          ko-KR	          |ko-KR|
 Malay   	               |          ms-MY           |    ms-MY|
 Portuguese	             |          pt-PT           |pt-PT|
 Portuguese, Brazilian	  |          pt-BR           |pt-BR   |
 Russian	                |          ru-RU           | ru-RU  |
 Spanish	                |          es-ES           | es-ES   |
 Spanish, US	            |          es-US           | es-US  |
 Tamil	                  |          ta-IN           |  ta-IN |
 Telugu	                 |          te-IN           |te-IN  |
 Thai	                   |          th-TH           | th-TH |
 Turkish	                |          tr-TR           |tr-TR|


When  selecting a ``region`` parameter it is recommended to use
``eu-west-1`` for best success.


FAST API REDOCS DOCS
* how to stop it
* how to use it
* how to see the documentation with docs and redoc

How to enable the service for google and aws given the previous readmes

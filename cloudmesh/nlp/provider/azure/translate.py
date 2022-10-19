from datetime import datetime
import uuid
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.util import readfile
from cloudmesh.common.Shell import Shell
import requests
import os

import yaml

# Proposal 

spec = """
name: aws-translate
region: translate.google.com
function: translate
   from: en
   to: de
"""

# FOR AZURE CREDENTIAL KEY: export AZURE_API_KEY="SDFJHW"

# from googletrans import Translator

# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')

# for translation in translations:
#     print(translation.origin, ' -> ', translation.text)

# Language detection
# The detect method, as its name implies, identifies the language used in a given sentence.
#
# translator.detect('This sentence is written in English.')
# <Detected lang=en confidence=0.22348526>


# translator.translate('veritas lux mea', src='la')


class Translate:
    def __init__(self, region="region", spec=None):
        json_file = Shell.map_filename('~/.cloudmesh/nlp/azure.dat').path
        api_and_location = [line.split(':', 1) for line in open(json_file)]
        api_and_location = dict(api_and_location)
        self.api_key = api_and_location['apikey'].strip()
        self.location = api_and_location['location'].strip()
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file
        # azure_api_key = os.environ["AZURE_API_KEY"]
        # print("aaaaaaaaa", azure_api_key)

        if spec is None:
            # self.service = DocumentTranslationClient("https://api.cognitive.microsofttranslator.com/", AzureKeyCredential(api_key))
            pass
        else:

            self.data = yaml.loads(spec)
            # self.service = Translator()

            # translator = Translator(service_urls=[
            #      'translate.google.com',
            #      'translate.google.co.kr',
            #    ])

            self.source_language_code = self.data["function"]["from"]
            self.tagret_language_code = self.data["function"]["to"]

    def get(self, content, SourceLanguageCode="en", TargetLanguageCode="de"):

        # poller = self.service.begin_translation("<sas_url_to_source>", "<sas_url_to_target>",
        #                                         "<target_language_code>")
        #
        # result = " ???"  # read from poller
        # # then convert to data
        # data = {
        #     "content": content,
        #     "SourceLanguageCode": SourceLanguageCode,
        #     "TargetLanguageCOde": TargetLanguageCode,
        #     "TranslatedText": result
        # }

        # Indicate that we want to translate and the API
        # version (3.0) and the target language
        endpoint = 'https://api.cognitive.microsofttranslator.com/'
        path = '/translate?api-version=3.0'

        # Add the target language parameter
        target_language_parameter = f'&to={TargetLanguageCode}'

        source_language_parameter = f'&from={SourceLanguageCode}'

        # Create the full URL
        constructed_url = endpoint + path + source_language_parameter + target_language_parameter

        # Set up the header information, which includes our
        # subscription key
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # Create the body of the request with the text to be
        # translated
        body = [{'text': content}]

        # Make the call using post
        StopWatch.start('translate')
        translator_request = requests.post(
            constructed_url, headers=headers, json=body)
        StopWatch.stop('translate')

        now = datetime.now()

        # Retrieve the JSON response
        translator_response = translator_request.json()

        # Retrieve the translation
        translated_text = translator_response[0]['translations'][0]['text']

        # Call render template, passing the translated text,
        # original text, and target language to the template

        # #
        # # just for debugging will be removed
        # #
        # print('TranslatedText: ' + result.get('TranslatedText'))
        # print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
        # print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
        data = {
            'input': content,
            'input_language': SourceLanguageCode,
            'output_language': TargetLanguageCode,
            'output': translated_text,
            # 'date':            result['ResponseMetadata']['HTTPHeaders']['date']
            'date': now.strftime("%m/%d/%Y %H:%M:%S"),
            'time': StopWatch.get('translate'),
            'provider': 'azure'
        }

        return data

    # not sure if available in azure please research
    # def detect(self, content):
    #    result = self.service.detect(content)
    #    return result
    #    # <Detected lang=en confidence=0.22348526>

# s = Translate()
# r = s.get("Hello world")
# r = s.get("Hallo  Welt", SourceLanguageCode="de", TargetLanguageCode="en")

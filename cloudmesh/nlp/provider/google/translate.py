
import six
from google.cloud import translate_v2 as translate

import yaml 

# Proposal 

spec = """
name: aws-translate
region: translate.google.com
function: translate
   from: en
   to: de
"""

#https://www.linode.com/docs/guides/documenting-a-fastapi-app-with-openapi/

# from googletrans import Translator

# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')

# for translation in translations:
#     print(translation.origin, ' -> ', translation.text)

# Language detection
# The detect method, as its name implies, identifies the language used in a given sentence.

# translator.detect('This sentence is written in English.')
# <Detected lang=en confidence=0.22348526>

# please replace with
# see https://cloud.google.com/translate/docs/setup#client_libraries
# it does need authentication

class Translate:
    def __init__(self, region=None, spec=None):
        # ignore the region
        print ("OOOO")
        if spec is None:
            self.service = translate.Client()
        else:

            self.data = yaml.loads(spec)
            self.service = self.service = translate.Client()

            # translator = Translator(service_urls=[
            #      'translate.google.com',
            #      'translate.google.co.kr',
            #    ]

            self.source_language_code = self.data["function"]["from"]
            self.tagret_language_code = self.data["function"]["to"]


    def get(self, content, SourceLanguageCode="en", TargetLanguageCode="de"):
        print(SourceLanguageCode)
        print(TargetLanguageCode)

        if isinstance(content, six.binary_type):
            content = content.decode("utf-8")

        result = self.service.translate(content, target_language=TargetLanguageCode)

        print ("AAA", result)

        data = {
            "content": result["input"],
            "SourceLanguageCode": SourceLanguageCode,
            "TargetLanguageCode": TargetLanguageCode,
            "TranslatedText": result["translatedText"],
            "detectedSourceLanguage": result["detectedSourceLanguage"],
        }


        # just for debugging will be removed

        print('TranslatedText: ' + data.get('TranslatedText'))
        print('SourceLanguageCode: ' + data.get('SourceLanguageCode'))
        print('TargetLanguageCode: ' + data.get('TargetLanguageCode'))

        print("Detected source language: " + data.get("detectedSourceLanguage"))

        return result

    def detect(self, content):
        result = self.service.detect(content)
        return result
        # <Detected lang=en confidence=0.22348526>

# s = Translate()
# r = s.get("Hello world")
# r = s.get("Hallo  Welt", SourceLanguageCode="de", TargetLanguageCode="en")



from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient
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
        azure_api_key = os.environ["AZURE_API_KEY"]
        print("aaaaaaaaa", azure_api_key)

        if spec is None:
            self.service = DocumentTranslationClient("<endpoint>", AzureKeyCredential("<api_key>"))
        else:

            self.data = yaml.loads(spec)
            self.service = self.service = Translator()

            # translator = Translator(service_urls=[
            #      'translate.google.com',
            #      'translate.google.co.kr',
            #    ])

            self.source_language_code = self.data["function"]["from"]
            self.tagret_language_code = self.data["function"]["to"]

    def get(self, content, SourceLanguageCode="en", TargetLanguageCode="de"):

        poller = self.service.begin_translation("<sas_url_to_source>", "<sas_url_to_target>",
                                                "<target_language_code>")

        result = " ???"  # read from poller
        # then convert to data
        data = {
            "content": content,
            "SourceLanguageCode": SourceLanguageCode,
            "TargetLanguageCOde": TargetLanguageCode,
            "TranslatedText": result
        }

        #
        # just for debugging will be removed
        #
        print('TranslatedText: ' + result.get('TranslatedText'))
        print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
        print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

        return result

    # not sure if available in azure please research
    # def detect(self, content):
    #    result = self.service.detect(content)
    #    return result
    #    # <Detected lang=en confidence=0.22348526>

# s = Translate()
# r = s.get("Hello world")
# r = s.get("Hallo  Welt", SourceLanguageCode="de", TargetLanguageCode="en")

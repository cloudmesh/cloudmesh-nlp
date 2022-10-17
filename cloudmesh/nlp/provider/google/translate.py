from datetime import datetime
from cloudmesh.common.StopWatch import StopWatch
import six
import yaml
from google.cloud import translate_v2 as translate
from google.cloud import language
from cloudmesh.common.Shell import Shell
import os


json_file = Shell.map_filename('~/.cloudmesh/nlp/cloudmesh.json').path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=json_file
client = language.LanguageServiceClient.from_service_account_json(json_file)

# Proposal 

spec = """
name: aws-translate
region: translate.google.com
function: translate
   from: en
   to: de
"""


# https://www.linode.com/docs/guides/documenting-a-fastapi-app-with-openapi/

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

        if spec is None:
            self.service = translate.Client()
        else:
            self.data = yaml.loads(spec)
            self.service = self.service = translate.Client()
            self.source_language_code = self.data["function"]["from"]
            self.target_language_code = self.data["function"]["to"]

    def get(self, content, SourceLanguageCode="en", TargetLanguageCode="de"):

        if isinstance(content, six.binary_type):
            content = content.decode("utf-8")

        StopWatch.start('translate')
        result = self.service.translate(content, target_language=TargetLanguageCode)
        StopWatch.stop('translate')

        now = datetime.now()

        print(type(result))

        data = {

            'input': result["input"],
            'input_language': SourceLanguageCode,
            'output_language': TargetLanguageCode,
            'output': result["translatedText"],
            'date': now.strftime("%m/%d/%Y %H:%M:%S"),
            'time': StopWatch.get('translate'),
            'provider': 'google'

        }
        return data

    def detect(self, content):
        result = self.service.detect(content)
        return result
        # <Detected lang=en confidence=0.22348526>

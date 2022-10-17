from datetime import datetime
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import six
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.util import readfile
from cloudmesh.common.Shell import Shell
from dotenv import load_dotenv
import os

class Translate:

    def __init__(self):
        ibm_file = Shell.map_filename('~/.cloudmesh/nlp/ibm-credentials.env').path
        load_dotenv(ibm_file)


        apikey = os.getenv('LANGUAGE_TRANSLATOR_APIKEY')
        url = os.getenv('LANGUAGE_TRANSLATOR_URL')
        #authenticate

        authenticator = IAMAuthenticator(apikey)

        #setup service
        self.lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

        self.lt.set_service_url(url)

        #authenticate

        authenticator = IAMAuthenticator(apikey)

    def get(self, content, SourceLanguageCode="en", TargetLanguageCode="de"):

        if isinstance(content, six.binary_type):
            content = content.decode("utf-8")
        print("hi :)")
        StopWatch.start('translate')
        result = self.lt.translate(
            text=f'{content}', model_id=f'{SourceLanguageCode}-{TargetLanguageCode}').get_result()
        StopWatch.stop('translate')
        print('hereitis')
        print(result)
        print('done')
        now = datetime.now()

        print(type(result))

        data = {

            'input': content,
            'input_language': SourceLanguageCode,
            'output_language': TargetLanguageCode,
            'output': result['translations'][0]['translation'],
            'date': now.strftime("%m/%d/%Y %H:%M:%S"),
            'time': StopWatch.get('translate'),
            'provider': 'ibm'

        }
        return data
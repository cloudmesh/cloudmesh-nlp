from datetime import datetime
from cloudmesh.common.StopWatch import StopWatch
import boto3
import yaml

# Proposal

spec = """
name: aws-translate
region:: us-east-1
function: translate
   from: en
   to: de
"""


class Translate:

    def __init__(self, region="us-east-1", spec=None):
        if spec is None:
            self.service = boto3.client(service_name='translate', region_name=region, use_ssl=True)
        else:
            self.data = yaml.loads(spec)
            self.service = boto3.client(service_name='translate', region_name=self.data["region"], use_ssl=True)
            self.source_language_code = self.data["function"]["from"]
            self.target_language_code = self.data["function"]["to"]

    def get(self, content, SourceLanguageCode="en", TargetLanguageCode="de"):

        StopWatch.start('translate')
        result = self.service.translate_text(Text=content,
                                             SourceLanguageCode=SourceLanguageCode,
                                             TargetLanguageCode=TargetLanguageCode)
        
        StopWatch.stop('translate')


        now = datetime.now()

        data = {
            'input': content,
            'input_language': result.get('SourceLanguageCode'),
            'output_language': result.get('TargetLanguageCode'),
            'output': result.get('TranslatedText'),
            # 'date':            result['ResponseMetadata']['HTTPHeaders']['date']
            'date': now.strftime("%m/%d/%Y %H:%M:%S"),
            'time':   StopWatch.get('translate'),
            'provider': 'aws'
        }

        return data

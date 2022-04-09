import boto3
import yaml 

# Proposal 

spec = """
name: aws-translate
region:: US-east
function: translate
   from: en
   to: de
"""

class Translate:
    def __init__(self, region="region", spec=None):
        if spec is None:
            self.service = boto3.client(service_name='translate', region_name=region, use_ssl=True)
        else:
            self.data = yaml.loads(spec)
            self.service = boto3.client(service_name='translate', region_name=self.data["region"], use_ssl=True)
            self.source_language_code = self.data["function"]["from"]
            self.tagret_language_code = self.data["function"]["to"]


    def get(self, content, SourceLanguageCode="en", TargetLanguageCode="de"):

        result = self.service.translate_text(Text=content, 
                    SourceLanguageCode=SourceLanguageCode, TargetLanguageCode=TargetLanguageCode)
        print('TranslatedText: ' + result.get('TranslatedText'))
        print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
        print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

        return result



# s = Translate()
# r = s.get("Hello world")
# r = s.get("Hallo  Welt", SourceLanguageCode="de", TargetLanguageCode="en")



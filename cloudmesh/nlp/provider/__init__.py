from cloudmesh.nlp.provider import ibm
from cloudmesh.nlp.provider import aws
from cloudmesh.nlp.provider import google


class Translate:

    def __init__(self, provider):
        self.provider = None
        if provider == 'ibm':
            from cloudmesh.nlp.provider.ibm.translate import Translate
        elif provider == 'aws':
            from cloudmesh.nlp.provider.aws.translate import Translate
        elif provider == 'google':
            from cloudmesh.nlp.provider.google.translate import Translate
        self.provider = Translate


    def get(self, content, SourceLanguageCode="en", TargetLanguageCode="de"):
        data = self.provider.get(content, SourceLanguageCode=SourceLanguageCode, TargetLanguageCode=TargetLanguageCode)
        return data
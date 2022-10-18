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
        else:
            Translate = None
        self.provider = Translate
        self.translator = Translate()

    def get(self, content, SourceLanguageCode="en", TargetLanguageCode="de"):
        data = self.provider.get(self=self.translator, content=content, SourceLanguageCode=SourceLanguageCode, TargetLanguageCode=TargetLanguageCode)
        return data
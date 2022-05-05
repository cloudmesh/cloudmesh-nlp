import os
from pprint import pprint

from cloudmesh.common.console import Console
from cloudmesh.common.debug import VERBOSE
from cloudmesh.nlp.nlp import Nlp
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.shell.command import map_parameters


class NlpCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_nlp(self, args, arguments):
        """
        ::

          Usage:
                nlp start
                nlp stop
                nlp status
                nlp info
                nlp run [--source=SOURCE] [--output=OUTPUT] [--parameter=PARAMETER] [TEXT]
                nlp translate [--provider=PROVIDER] [--from=FROM] [--to=TO] [--region=REGION] TEXT...
                nlp deploy --provider=PROVIDER

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file
              --source=SOURCE        tbd
              --output=OUTPUT        tbd
              --parameter=PARAMETER  tbd
              --provider=PROVIDER    A cloud provider to execute the natural
                                     language processing service such as
                                     aws, google
                                     [default: aws]
              --from=FROM            To letter/language code representing
                                     the text in which it is written.
                                     [default: en]
              --to=TO                The Letter/language code representing
                                     what the text is going to be translated to.
                                     [default: de]
              --region=REGION        A cloud provider can run this language
                                     translation in multiple regions here you
                                     may specify what region applies to you.

        """

        # arguments.FILE = arguments['--file'] or None

        map_parameters(arguments,
                       "source",
                       "output",
                       "parameter",
                       "provider")

        # VERBOSE(arguments)

        nlp = Nlp()

        if arguments.start:
            nlp.start()
        elif arguments.stop:
            nlp.stop()
        elif arguments.status:
            nlp.status()
        elif arguments.info:
            nlp.info()
        elif arguments.run:
            "nlp run [--source=SOURCE] [--output=OUTPUT] [--parameter=PARAMETER] [TEXT]"
            r = nlp.run(source=arguments.source,
                        output=arguments.output,
                        parameter=arguments.parameter,
                        text=arguments.TEXT)
            print(r)
        #
        #  DEPLOY
        #
        elif arguments.deploy:

            provider = arguments.provider.lower()

            if provider == "aws":
                Console.error("pip install boto3")

            elif provider == "azure":
                # see https://docs.microsoft.com/en-us/python/api/overview/azure/ai-translation-document-readme?view=azure-python-preview

                os.system("pip install azure-ai-translation-document --pre")
                os.system("pip install azure-identity")
                # also install az
                # az group create --name my-resource-group --location westus2
                # az cognitiveservices account create \
                #     --name document-translation-resource \
                #     --custom-domain document-translation-resource \
                #     --resource-group my-resource-group \
                #     --kind TextTranslation \
                #     --sku S1 \
                #     --location westus2 \
                #     --yes
                # az cognitiveservices account keys list --name "resource-name" --resource-group "resource-group-name"
                # from azure.core.credentials import AzureKeyCredential
                # from azure.ai.translation.document import DocumentTranslationClient
                #
                # endpoint = "https://<resource-name>.cognitiveservices.azure.com/"
                # credential = AzureKeyCredential("<api_key>")
                # document_translation_client = DocumentTranslationClient(endpoint, credential)
                # from azure.identity import DefaultAzureCredential
                # from azure.ai.translation.document import DocumentTranslationClient
                # credential = DefaultAzureCredential()
                #
                # document_translation_client = DocumentTranslationClient(
                #     endpoint="https://<resource-name>.cognitiveservices.azure.com/",
                #     credential=credential
                # )

            elif provider == "google":
                print("AAA")
                os.system("pip install googletrans")

            else:
                Console.provider("Not implemented")

        #
        # TRANSLATE
        elif arguments.translate:

            try:
                provider = arguments.provider.lower()

                from_language = arguments["--from"]
                to_language = arguments["--to"]
                content = " ".join(arguments.TEXT)
                #
                # load the right Translate class
                #
                if provider == "aws":
                    from cloudmesh.nlp.provider.aws.translate import Translate
                    if arguments.region is None:
                        arguments.region = "us-east-1"

                elif provider == "azure":

                    Console.error("Not implemented")

                elif provider == "google":
                    from cloudmesh.nlp.provider.google.translate import Translate

                else:
                    Console.provider("Not implemented")

                s = Translate(region=arguments.region)
                r = s.get(content, SourceLanguageCode=from_language, TargetLanguageCode=to_language)
                pprint(r)
            except Exception as e:
                print(e)

        else:
            Console.error("You must be giving a command parameter.")

        return ""

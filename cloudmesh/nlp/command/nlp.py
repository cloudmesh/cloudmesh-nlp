from ast import arg
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand

from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters
from cloudmesh.nlp.nlp import Nlp
import os

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
                nlp translate [--provider=PROVIDER] [--from=FROM] [--to=TO] [TEXT]
                nlp deploy --provider=PROVIDER

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """


        # arguments.FILE = arguments['--file'] or None

        map_parameters(arguments,
                       "source",
                       "output",
                       "parameter",
                       "deploy",
                       "translate")

        VERBOSE(arguments)

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
            print (r)
        #
        #  DEPLOY
        #
        elif arguments.deploy:

            provider = arguments.provider.lower()

            if provider == "aws":
                Console.error("pip install boto3")

            elif provider == "azure":
                Console.error("Not implemented")

            elif provider == "google":
                os.system("pip install googletrans")

            else:
                Console.provider("Not implemented")

        #
        # TRANSATE
        #
        elif arguments.translate:

            provider = arguments.provider.lower()

            from_language = arguments["--from"]
            to_language = arguments["--to"]

            #
            # load the right Translate class
            #
            if provider == "aws":
                from cloudmesh.nlp.provider.aws.translate import Translate

            elif provider == "azure":
                Console.error("Not implemented")

            elif provider == "google":
                Console.error("Not implemented")

            else:
                Console.provider("Not implemented")
    
            s = Translate()
            r = s.get("Hello world", SourceLanguageCode=from_language, TargetLanguageCode=to_language)


        else:
            Console.error("You must be giving a command parameter.")
        return ""

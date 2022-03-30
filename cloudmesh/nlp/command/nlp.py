from ast import arg
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand

from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters
from cloudmesh.nlp.nlp import Nlp

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
                nlp translate [--from=FROM] [--to=TO] [TEXT]

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """


        # arguments.FILE = arguments['--file'] or None

        map_parameters(arguments, "file", "source", "output", "parameter", "translate")

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
        elif arguments.translate:
            if arguments.provider.lower() == "aws":
                from cloudmesh.nlp.provider.aws.translate import Translate  
            elif arguments.provider.lower() == "azure":
                Console.error("Not implemented")
            else:
                Console.provider("Not implemented")
    
            s = Translate()
            r = s.get("Hello world")
            r = s.get("Hallo  Welt", SourceLanguageCode="de", TargetLanguageCode="en")


        else:
            Console.error("You must be giving a command parameter.")
        return ""

from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.nlp.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters

class NlpCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_nlp(self, args, arguments):
        """
        ::

          Usage:
                nlp --file=FILE
                nlp list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """


        # arguments.FILE = arguments['--file'] or None

        map_parameters(arguments, "file")

        VERBOSE(arguments)

        m = Manager()

        if arguments.file:
            print("option a")
            m.list(path_expand(arguments.file))

        elif arguments.list:
            print("option b")
            m.list("just calling list without parameter")

        Console.error("This is just a sample")
        return ""

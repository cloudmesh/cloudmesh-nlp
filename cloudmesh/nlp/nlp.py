"""
                nlp start
                nlp stop
                nlp status
                nlp info
                nlp run [--source=SOURCE] [--output=OUTPUT] [--parameter=PARAMETER] [TEXT]

"""


class Nlp:

    def start(self):
        print("start")
        # TODO: figure out how to start service


    def stop(self):
        print("stop")
        # TODO: figure out how to stop service

    def info(self):
        print("info")
        # TODO: figure out how to acquire info on service

    def status(self):
        print("status")
        # TODO: figure out how to acquire status

    def run(self, source=None, output=None, parameter=None, text=None):
        print(f"Text: {text}")
        print("run")
        result = ""

        # do the processing
        # end processing

        return result

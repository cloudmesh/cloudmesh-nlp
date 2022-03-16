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

    def stop(self):
        print("stop")

    def info(self):
        print("info")

    def status(self):
        print("status")

    def run(self, source=None, output=None, parameter=None, text=None):
        print (f"Text: {text}")
        print("run")
        result = ""

        # do the processing

        result = {"german" : "Hallo",
                  "english": "Hello"}

        # end processing


        return result
import pkg_resources
from cloudmesh.common.Shell import Shell
"""
                nlp start
                nlp stop
                nlp doc
                nlp status
                nlp info
                nlp run [--source=SOURCE] [--output=OUTPUT] [--parameter=PARAMETER] [TEXT]

"""


class Nlp:

    def start(self, reload: bool = False):
        print("start")
        cloudmesh_nlp = pkg_resources.resource_filename("cloudmesh.nlp",
                                                        "../..")
        host = "127.0.0.1"
        port = 8000

        print("Reload:", reload)
        print("Dir:", cloudmesh_nlp)
        import uvicorn

        uvicorn.run("cloudmesh.nlp.s:app",
                    host=host,
                    port=port,
                    workers=1,
                    reload=reload,
                    reload_dirs=[cloudmesh_nlp])


    def stop(self):
        print("stop")
        # TODO: figure out how to stop service

    def doc(self):
        host = "127.0.0.1"
        port = 8000
        url = f"http://{host}:{port}/docs"
        Shell.browser(url)

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

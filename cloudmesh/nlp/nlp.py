import pkg_resources
from cloudmesh.common.Shell import Console
from cloudmesh.common.Shell import Shell
from cloudmesh.common.systeminfo import os_is_windows
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
        if os_is_windows():
            import psutil
            import ctypes

            if ctypes.windll.shell32.IsUserAnAdmin() == 0:
                Console.error("Please run as admin")
                return False

            cms_ids = []
            # Iterate over all running processes
            for proc in psutil.process_iter():
                if proc.name() == 'cms.exe':
                    cms_ids.append(proc.pid)

            # this is necessary or else the prg will attempt
            # to terminate itself. since there are two cms.exe,
            # we must end the one started earlier
            if len(cms_ids) != 1:
                if psutil.Process(cms_ids[0]).create_time() > psutil.Process(
                        cms_ids[1]).create_time():
                    cms_ids.remove(cms_ids[0])
                else:
                    cms_ids.remove(cms_ids[1])
            try:
                Shell.run(fr'taskkill /PID {cms_ids[0]} /F /T')
                Console.ok('Server successfully killed')
                return True
            except Exception as e:
                print(e)
                return False

        else:
            Shell.run('kill $(pgrep -f "cms nlp start")')

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

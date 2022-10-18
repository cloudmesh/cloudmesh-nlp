###############################################################
# pytest -v --capture=no benchmarks/test_benchmark.py
# pytest -v  benchmarks/test_benchmark.py
# pytest -v --capture=no  benchmarks/test_benchmark.py::TestConfig::<METHODNAME>
###############################################################
import pytest
import os
from cloudmesh.common.Benchmark import Benchmark
from cloudmesh.common.Shell import Shell
from cloudmesh.common.dotdict import dotdict
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
from cloudmesh.common.systeminfo import get_platform
from cloudmesh.nlp.provider import Translate
import requests
# provider = ['google', 'aws', 'azure', 'ibm']
provider = ['google', 'aws']
text = 'hello'
n = 20
node = get_platform()
user = 'gregor'

@pytest.mark.incremental
class TestConfig:

    def test_help(self):
        HEADING()
        # Benchmark.Start()
        result = Shell.execute("cms help", shell=True)
        # Benchmark.Stop()
        VERBOSE(result)

        assert "quit" in result
        assert "clear" in result

    def test_cli(self):
        HEADING()
        global text
        global provider
        global n
        for p in provider:
            for i in range(n):
                result = None
                print(f"experiment {i}")
                StopWatch.start(f"{p}-{text}-{i}-cli")
                result = Shell.run(f"cms nlp translate --provider={p} --to=de --from=en {text}")
                StopWatch.stop(f"{p}-{text}-{i}-cli")
                assert "hallo" in result
            VERBOSE(result)

    def test_api(self):
        HEADING()
        global text
        global provider
        global n

        for p in provider:
            translator = Translate(provider=p)
            for i in range(n):
                result = None
                print(f"experiment {i}")
                StopWatch.start(f"{p}-{text}-{i}-api")
                result = translator.get(content=text,
                                        SourceLanguageCode='en',
                                        TargetLanguageCode='de')

                StopWatch.stop(f"{p}-{text}-{i}-api")
                assert "hallo" in result['output']
            VERBOSE(result)

    def test_requests(self):
        HEADING()
        global text
        global provider
        global n

        for p in provider:
            for i in range(n):
                result = None
                print(f"experiment {i}")
                StopWatch.start(f"{p}-{text}-{i}-requests")
                result = requests.get(f'http://localhost:8000/translate/{text}?provider={p}&fromlang=en&tolang=de')
                StopWatch.stop(f"{p}-{text}-{i}-requests")
                assert "hallo" in result.text
            VERBOSE(result)


    # def test_region(self):
    #     HEADING()
    #     Benchmark.Start()
    #     result = Shell.run(f"cms nlp translate --region=us-east-1 --provider={provider} --to=de --from=en hello")
    #     Benchmark.Stop()
    #     VERBOSE(result)
    #
    #     assert "hallo" in result

    def test_benchmark(self):
        HEADING()
        node = get_platform()
        data = {}
        data["node"] = get_platform()
        data["user"] = user
        data["text"] = text

        Benchmark.print(csv=True, sysinfo=False, tag=str(data), node=node, user=user)
        if not os.path.isdir("./results"):
            Shell.mkdir("./results")
        StopWatch.benchmark(csv=True, sysinfo=False, tag=str(data), node=node,
                            user=user, filename=f'./results/{text}.log')

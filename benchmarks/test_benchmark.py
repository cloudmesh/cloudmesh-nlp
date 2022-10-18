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
# provider = ['google', 'aws', 'azure', 'ibm']
provider = ['ibm']
text = 'hello'
n=1
node = get_platform()
user = 'gregor'

@pytest.mark.incremental
class TestConfig:

    def test_help(self):
        HEADING()
        Benchmark.Start()
        result = Shell.execute("cms help", shell=True)
        Benchmark.Stop()
        VERBOSE(result)

        assert "quit" in result
        assert "clear" in result

    def test_google(self):
        HEADING()
        global text
        global provider
        global n
        for p in provider:
            for i in range(n):
                result = None
                print(f"experiment {i}")
                StopWatch.start(f"{p}-{text}-{i}")
                result = Shell.run(f"cms nlp translate --provider={p} --to=de --from=en {text}")
                StopWatch.stop(f"{p}-{text}-{i}")
                assert "hallo" in result
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
                            user=user, filename=f'results/{provider}-{text}.log')

###############################################################
# pytest -v --capture=no tests/test_google.py
# pytest -v  tests/test_google.py
# pytest -v --capture=no  tests/test_google.py::Test_nlp::<METHODNAME>
###############################################################
import pytest
from cloudmesh.common.Benchmark import Benchmark
from cloudmesh.common.Shell import Shell
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING

provider='google'

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
        Benchmark.Start()
        result = Shell.run(f"cms nlp translate --provider={provider} --to=de --from=en hello")
        Benchmark.Stop()
        VERBOSE(result)

        assert "hallo" in result

    def test_region(self):
        HEADING()
        Benchmark.Start()
        result = Shell.run(f"cms nlp translate --region=us-east-1 --provider={provider} --to=de --from=en hello")
        Benchmark.Stop()
        VERBOSE(result)

        assert "hallo" in result

    def test_benchmark(self):
        HEADING()
        Benchmark.print(csv=True, sysinfo=False, tag="cmd5")

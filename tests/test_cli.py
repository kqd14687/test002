import subprocess
import sys

from test002 import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "test002", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__

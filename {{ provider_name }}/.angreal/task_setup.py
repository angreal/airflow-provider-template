import angreal
from angreal.integrations.venv import venv_required

import os
import subprocess

venv_location = os.path.join(angreal.get_root(),'..','.venv')
cwd = os.path.join(angreal.get_root(), '..')

@angreal.command(name='dev-setup', about="setup a development environment")
def setup_env():
    VirtualEnv(venv_location, now=True, requirements=".[dev]")
    subprocess.run(
        (
        "pre-commit install;"
        "pre-commit run --all-files;"
        ),
        shell=True,
        cwd=cwd
    )
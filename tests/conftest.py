
from subprocess import check_call

import pytest
import random
from hashlib import sha1


@pytest.fixture
def virtual_env_path(tmpdir):

    venv = tmpdir.join('venv')

    check_call(['virtualenv', str(tmpdir.join('venv'))], cwd=str(tmpdir))

    venv.mkdir('run')
    venv.mkdir('log')
    venv.mkdir('tmp')

    return venv


@pytest.fixture
def virtual_env(virtual_env_path):
    class VirtualENVInstalationError(Exception):
        "Virltual error"

    class VirtualENV(object):
        def __init__(self, path):
            self.path = path

        def install_package(self, package):

            log_name = sha1("%s-%s" % (random.randint(0, 100), package)).hexdigest() + '-install.log'
            log_path = self.path.join('tmp', log_name)

            log_path.write('')
            install_log = log_path.open(mode='r+w')

            try:
                check_call([str(self.path.join('bin', 'pip')), 'install', package], stdout=install_log)
            except:
                install_log.flush()
                install_log.seek(0)
                raise VirtualENVInstalationError(install_log.read())
    return VirtualENV(path=virtual_env_path)

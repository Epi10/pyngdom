# The MIT License (MIT)
# Copyright (c) 2015 EPI10
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.#

import os
import sys

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

@pytest.fixture
def username():
    return os.getenv('PINGDOM_USERNAME', None)

@pytest.fixture
def password():
    return os.getenv('PINGDOM_PASSWORD', None)

@pytest.fixture
def rumid():
    id = os.getenv('PINGDOM_RUMID', None)
    if id is None:
        pytest.skip("No RUMID supplied")
    return id

@pytest.fixture
def driver(request, username, password):
    if username is None or password is None:
        pytest.skip("No username or password suppied to test pingdom (this is fine in travis)")

    from pyngdom import PyngdomDriver

    driver = PyngdomDriver(username=username, password=password)
    request.addfinalizer(driver.quit)
    driver.login()
    return driver

@pytest.fixture
def pingdom_rum(request, username, password):
    if username is None or password is None:
        pytest.skip("No username or password suppied to test pingdom (this is fine in travis)")

    from pyngdom import PyngdomRum

    driver = PyngdomRum(username=username, password=password)
    request.addfinalizer(driver.quit)
    driver.login()
    return driver


import os
import sys

from subprocess import check_call
from pyngdom import __version__


def test_dist_installation(virtual_env, tmpdir):

    check_call(['python', 'setup.py', 'sdist'], cwd=os.path.join(sys.path[0], '..'))

    pyngdom_dist = os.path.join(sys.path[0], '..', 'dist', 'pyngdom-%s.tar.gz' % __version__)

    virtual_env.install_package(pyngdom_dist)

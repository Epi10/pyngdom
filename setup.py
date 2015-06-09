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
from distutils.core import setup

from pyngdom import __version__

try:
    f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
    long_description = f.read()
    f.close()
except:
    long_description = ''

setup(
    name='pyngdom',
    version=__version__,
    packages=['pyngdom'],
    author='Alvaro Leiva',
    author_email='aleivag@gmail.com',
    url='https://github.com/Epi10/pyngdom',
    download_url='https://github.com/Epi10/pyngdom/releases/tag/%s' % __version__,
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Topic :: System :: Monitoring"
    ],
    keywords=['monitoring', 'rum', 'pingdom'],
    description='A simple pingdom API interface for read RUM information',
    long_description=long_description,
    license='MIT'
)

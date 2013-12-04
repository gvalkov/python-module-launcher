#!/usr/bin/env python
# encoding: utf-8

from os.path import abspath, dirname, join as pjoin
from sys import version_info
from setuptools import setup

here = abspath(dirname(__file__))

classifiers = (
    'Development Status :: 3 - Alpha',
    # 'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Operating System :: POSIX :: Linux',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
)

console_scripts = [
    'python-module-launcher-{0.major}.{0.minor} = modulelauncher:main'\
    .format(version_info)]

kw = {
    'name'              : 'module-launcher',
    'version'           : '0.1.0',
    'description'       : 'Preforks interpreters to reduce script startup time',
    'long_description'  : open(pjoin(here, 'README.rst')).read(),
    'author'            : 'Georgi Valkov',
    'author_email'      : 'georgi.t.valkov@gmail.com',
    'license'           : 'Revised BSD License',
    'keywords'          : 'module launcher speedup prefork',
    'classifiers'       : classifiers,
    'url'               : 'https://github.com/gvalkov/python-module-launcher',
    'entry_points'      : {'console_scripts' : console_scripts},
    'py_modules'        : ['modulelauncher'],
    'install_requires'  : ['argparse', 'python-daemon'],
    'zip_safe'          : True,
}

if __name__ == '__main__':
    setup(**kw)

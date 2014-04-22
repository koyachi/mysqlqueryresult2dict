from setuptools import setup, find_packages
import os
import sys

libdir = 'mysqlqueryresult2dict'
#bindir = os.path.join('', 'bin')

sys.path.insert(0, libdir)

import info
import version

setup_options = info.INFO
setup_options["version"] = version.VERSION
setup_options.update(dict(
    install_requires = open('requirements.txt').read().splitlines(),
#    scripts = ...
#    packages = find_packages(libdir),
    packages = find_packages(),
#    package_dir = {"": libdir},
))

setup(**setup_options)

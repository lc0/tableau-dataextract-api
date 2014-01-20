# -----------------------------------------------------------------------
# Copyright (c) 2012 Tableau Software, Incorporated
#                    and its licensors. All rights reserved.
# Protected by U.S. Patent 7,089,266; Patents Pending.
#
# Portions of the code
# Copyright (c) 2002 The Board of Trustees of the Leland Stanford
#                    Junior University. All rights reserved.
# -----------------------------------------------------------------------
# setup.py
# -----------------------------------------------------------------------
# WARNING: Computer generated file.  Do not hand modify.
from distutils.core import setup
import sys

# Skip the version check when building the source dist; we can
# patch things up later.
if len(sys.argv) < 2 or sys.argv[1] != 'sdist':
    if sys.version_info < (2, 7):
        print 'Python >= 2.7 required'
        exit(1)

setup(
    name='DataExtract',
    version='8000.13.0712.1936',
    packages=['dataextract'],
    package_data={'dataextract' : ['bin/*.*']},
    description="Create extracts for Tableau's Fast Data Engine",
    license='LICENSE.txt'
)

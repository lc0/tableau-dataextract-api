# -----------------------------------------------------------------------
# Copyright (c) 2012 Tableau Software, Incorporated
#                    and its licensors. All rights reserved.
# Protected by U.S. Patent 7,089,266; Patents Pending.
#
# Portions of the code
# Copyright (c) 2002 The Board of Trustees of the Leland Stanford
#                    Junior University. All rights reserved.
# -----------------------------------------------------------------------
# Libs.py
# -----------------------------------------------------------------------
# WARNING: Computer generated file.  Do not hand modify.

import ctypes
import os
import sys
os.environ['PATH'] = os.path.join(os.path.dirname(__file__), 'bin') + os.pathsep + os.environ['PATH']

if sys.platform == 'win32':
   LIB_PATH = 'DataExtract'
elif sys.platform.startswith('linux') or sys.platform.startswith('darwin') :
   LIB_PATH = os.path.join(os.path.dirname(__file__), 'lib', 'libDataExtract.so')
else:
   raise RuntimeError('Unknown platform ' + sys.platform)

class LoadLibs(object):
    def __init__(self, lib_path = LIB_PATH):
        self.lib = None
        self._is_lib_loaded = False
        self.lib_path = LIB_PATH

    @property
    def load_lib(self):
        if not self._is_lib_loaded:
            self.lib = ctypes.cdll.LoadLibrary(self.lib_path)
            self._is_lib_loaded = True
        return self.lib

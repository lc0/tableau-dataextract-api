# -----------------------------------------------------------------------
# Copyright (c) 2013 Tableau Software, Incorporated
#                    and its licensors. All rights reserved.
# Protected by U.S. Patent 7,089,266; Patents Pending.
#
# Portions of the code
# Copyright (c) 2002 The Board of Trustees of the Leland Stanford
#                    Junior University. All rights reserved.
# -----------------------------------------------------------------------
# StringUtils.py
# -----------------------------------------------------------------------

import ctypes
from . import Libs

libs = Libs.LoadLibs()
tablib = libs.load_lib

def ToTableauString(str):
    """Convert a Python string to a C TableauString"""

    wstr = ctypes.c_wchar_p(unicode(str))
    buffer = ctypes.create_string_buffer(ctypes.sizeof(ctypes.c_wchar) * (len(str) + 1))
    tablib.ToTableauString(wstr, ctypes.byref(buffer))
    return buffer

def FromTableauString(ts):
    """Convert a C TableauString to a Python string"""

    tslen = tablib.TableauStringLength(ts)
    buffer = ctypes.create_string_buffer((tslen + 1) * ctypes.sizeof(ctypes.c_wchar))
    tablib.FromTableauString(ts, ctypes.byref(buffer))
    return ctypes.wstring_at(buffer, tslen)

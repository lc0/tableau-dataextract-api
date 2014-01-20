# -----------------------------------------------------------------------
# Copyright (c) 2012 Tableau Software, Incorporated
#                    and its licensors. All rights reserved.
# Protected by U.S. Patent 7,089,266; Patents Pending.
# 
# Portions of the code
# Copyright (c) 2002 The Board of Trustees of the Leland Stanford
#                    Junior University. All rights reserved.
# -----------------------------------------------------------------------
# Exceptions.py
# -----------------------------------------------------------------------
class TableauException(Exception):
    def __init__(self, errorCode, message):
        Exception.__init__(self, message)
        self.errorCode = errorCode
        self.message = message

    def __str__(self):
        return 'TableauException ({0}): {1}'.format(self.errorCode, self.message)

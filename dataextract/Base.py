# -----------------------------------------------------------------------
# Copyright (c) 2012 Tableau Software, Incorporated
#                    and its licensors. All rights reserved.
# Protected by U.S. Patent 7,089,266; Patents Pending.
#
# Portions of the code
# Copyright (c) 2002 The Board of Trustees of the Leland Stanford
#                    Junior University. All rights reserved.
# -----------------------------------------------------------------------
# Base.py
# -----------------------------------------------------------------------
# WARNING: Computer generated file.  Do not hand modify.

from ctypes import *
from . import Exceptions
from . import Libs
from . import StringUtils
from . import Types

libs = Libs.LoadLibs()
tablib = libs.load_lib

class TableDefinition(object):
    """Represents a collection of columns, or more specifically name/type pairs."""

    def __init__(
        self
      , _handle = None
      , _parent = None
    ):
        """Creates an empty copy of a TableDefinition object, which represent a collection of columns."""

        if _handle != None:
            self._handle = _handle
            self._parent = _parent
            return

        self._handle = c_void_p(None)

        ret = tablib.TabTableDefinitionCreate(
            byref(self._handle)
        )

        if int(ret) != int(Types.Result.SUCCESS):
            raise Exceptions.TableauException(ret, wstring_at(tablib.TabGetLastErrorMessage()))

    def close(self):
        """Closes the TableDefinition object and frees associated memory."""
        if self._handle != None:
            tablib.TabTableDefinitionClose( self._handle )
            self._handle = None

    def __del__(self):
        self.close()

    def getDefaultCollation(
        self
    ):
        """Gets the current default collation; if unspecified, default is binary."""

        retval = c_int()
        result = tablib.TabTableDefinitionGetDefaultCollation(
            self._handle
          , byref(retval)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

        return retval.value

    def setDefaultCollation(
        self
      , collation
    ):
        """Sets the default collation for added string columns."""

        result = tablib.TabTableDefinitionSetDefaultCollation(
            self._handle
          , c_int(collation)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def addColumn(
        self
      , name
      , type
    ):
        """Adds a column to the table definition; the order in which columns are added implies their column number. String columns are defined with the current default collation."""

        if name == None:
            raise ValueError('name must not be None')

        result = tablib.TabTableDefinitionAddColumn(
            self._handle
          , StringUtils.ToTableauString(name)
          , c_int(type)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def addColumnWithCollation(
        self
      , name
      , type
      , collation
    ):
        """Adds a column with a specific collation."""

        if name == None:
            raise ValueError('name must not be None')

        result = tablib.TabTableDefinitionAddColumnWithCollation(
            self._handle
          , StringUtils.ToTableauString(name)
          , c_int(type)
          , c_int(collation)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def getColumnCount(
        self
    ):
        """Returns the number of columns in the table definition."""

        retval = c_int()
        result = tablib.TabTableDefinitionGetColumnCount(
            self._handle
          , byref(retval)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

        return retval.value

    def getColumnName(
        self
      , columnNumber
    ):
        """Gives the name of the column."""

        retval = c_void_p(None)
        result = tablib.TabTableDefinitionGetColumnName(
            self._handle
          , c_int(columnNumber)
          , byref(retval)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

        return StringUtils.FromTableauString(retval)

    def getColumnType(
        self
      , columnNumber
    ):
        """Gives the type of the column."""

        retval = c_int()
        result = tablib.TabTableDefinitionGetColumnType(
            self._handle
          , c_int(columnNumber)
          , byref(retval)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

        return retval.value

    def getColumnCollation(
        self
      , columnNumber
    ):
        """Gives the collation of the column."""

        retval = c_int()
        result = tablib.TabTableDefinitionGetColumnCollation(
            self._handle
          , c_int(columnNumber)
          , byref(retval)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

        return retval.value

class Row(object):
    """A tuple of values to be inserted into an extract."""

    def __init__(
        self
      , tableDefinition
    ):
        """Create an empty row with the specified schema."""

        self._handle = c_void_p(None)

        ret = tablib.TabRowCreate(
            byref(self._handle)
          , tableDefinition._handle
        )

        if int(ret) != int(Types.Result.SUCCESS):
            raise Exceptions.TableauException(ret, wstring_at(tablib.TabGetLastErrorMessage()))

    def close(self):
        """Closes this Row and frees associated resources."""
        if self._handle != None:
            tablib.TabRowClose( self._handle )
            self._handle = None

    def __del__(self):
        self.close()

    def setNull(
        self
      , columnNumber
    ):
        """Sets a column in this row to null."""

        result = tablib.TabRowSetNull(
            self._handle
          , c_int(columnNumber)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def setInteger(
        self
      , columnNumber
      , value
    ):
        """Sets a column in this row to the specified integer value."""

        result = tablib.TabRowSetInteger(
            self._handle
          , c_int(columnNumber)
          , c_int(value)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def setDouble(
        self
      , columnNumber
      , value
    ):
        """Sets a column in this row to the specified double value."""

        result = tablib.TabRowSetDouble(
            self._handle
          , c_int(columnNumber)
          , c_double(value)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def setBoolean(
        self
      , columnNumber
      , value
    ):
        """Sets a column in this row to the specified boolean value."""

        result = tablib.TabRowSetBoolean(
            self._handle
          , c_int(columnNumber)
          , c_bool(value)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def setString(
        self
      , columnNumber
      , value
    ):
        """Sets a column in this row to the specified string value."""

        if value == None:
            raise ValueError('value must not be None')

        result = tablib.TabRowSetString(
            self._handle
          , c_int(columnNumber)
          , StringUtils.ToTableauString(value)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def setCharString(
        self
      , columnNumber
      , value
    ):
        """Sets a column in this row to the specified string value."""

        if value == None:
            raise ValueError('value must not be None')

        result = tablib.TabRowSetCharString(
            self._handle
          , c_int(columnNumber)
          , c_char_p(value)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def setDate(
        self
      , columnNumber
      , year
      , month
      , day
    ):
        """Sets a column in this row to the specified date value."""

        result = tablib.TabRowSetDate(
            self._handle
          , c_int(columnNumber)
          , c_int(year)
          , c_int(month)
          , c_int(day)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def setDateTime(
        self
      , columnNumber
      , year
      , month
      , day
      , hour
      , min
      , sec
      , frac
    ):
        """Sets a column in this row to the specified date/time value."""

        result = tablib.TabRowSetDateTime(
            self._handle
          , c_int(columnNumber)
          , c_int(year)
          , c_int(month)
          , c_int(day)
          , c_int(hour)
          , c_int(min)
          , c_int(sec)
          , c_int(frac)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def setDuration(
        self
      , columnNumber
      , day
      , hour
      , minute
      , second
      , frac
    ):
        """Sets a column in this row to the specified duration value."""

        result = tablib.TabRowSetDuration(
            self._handle
          , c_int(columnNumber)
          , c_int(day)
          , c_int(hour)
          , c_int(minute)
          , c_int(second)
          , c_int(frac)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

class Table(object):
    """A table in the extract."""

    def insert(
        self
      , row
    ):
        """Queue a row for insertion; may perform insert of buffered rows."""

        result = tablib.TabTableInsert(
            self._handle
          , row._handle
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

    def getTableDefinition(
        self
    ):
        """Get this table's schema."""

        retval = c_void_p(None)
        result = tablib.TabTableGetTableDefinition(
            self._handle
          , byref(retval)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

        return TableDefinition( _handle = retval, _parent = self)

    def __init__(self, _handle, _parent):
        """Internal use only: Create a new instance to wrap the specified handle."""
        self._handle = _handle
        self._parent = _parent

class Extract(object):
    """A Tableau Data Engine database."""

    def __init__(
        self
      , path
    ):
        """Create an extract object with an absolute or relative file system path. This object must be closed."""

        self._handle = c_void_p(None)

        if path == None:
            raise ValueError('path must not be None')

        ret = tablib.TabExtractCreate(
            byref(self._handle)
          , StringUtils.ToTableauString(path)
        )

        if int(ret) != int(Types.Result.SUCCESS):
            raise Exceptions.TableauException(ret, wstring_at(tablib.TabGetLastErrorMessage()))

    def close(self):
        """Closes the extract and any open tables."""
        if self._handle != None:
            tablib.TabExtractClose( self._handle )
            self._handle = None

    def __del__(self):
        self.close()

    def addTable(
        self
      , name
      , tableDefinition
    ):
        """Creates and adds table to the extract"""

        if name == None:
            raise ValueError('name must not be None')

        retval = c_void_p(None)
        result = tablib.TabExtractAddTable(
            self._handle
          , StringUtils.ToTableauString(name)
          , tableDefinition._handle
          , byref(retval)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

        return Table( _handle = retval, _parent = self)

    def openTable(
        self
      , name
    ):
        """Opens an existing table in the extract."""

        if name == None:
            raise ValueError('name must not be None')

        retval = c_void_p(None)
        result = tablib.TabExtractOpenTable(
            self._handle
          , StringUtils.ToTableauString(name)
          , byref(retval)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

        return Table( _handle = retval, _parent = self)

    def hasTable(
        self
      , name
    ):
        """Tests if a table exists in the extract."""

        if name == None:
            raise ValueError('name must not be None')

        retval = c_bool()
        result = tablib.TabExtractHasTable(
            self._handle
          , StringUtils.ToTableauString(name)
          , byref(retval)
        )

        if result != Types.Result.SUCCESS:
            raise Exceptions.TableauException(result, wstring_at(tablib.TabGetLastErrorMessage()))

        return retval.value

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

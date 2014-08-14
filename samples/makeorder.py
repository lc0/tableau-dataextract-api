# -----------------------------------------------------------------------
# The information in this file is the property of Tableau Software and
# is confidential.
#
# Copyright (C) 2012  Tableau Software.
# Patents Pending.
# -----------------------------------------------------------------------
# externalapi/samples/makeorder.py
# -----------------------------------------------------------------------
from datetime import datetime
import sys
from dataextract import *

# Define the table's schema
def makeTableDefinition():
    tableDef = TableDefinition()
    tableDef.setDefaultCollation(Collation.EN_GB)
    tableDef.addColumn('Purchased',       Type.DATETIME)
    tableDef.addColumn('Product',         Type.CHAR_STRING)
    tableDef.addColumn('uProduct',        Type.UNICODE_STRING)
    tableDef.addColumn('Price',           Type.DOUBLE)
    tableDef.addColumn('Quantity',        Type.INTEGER)
    tableDef.addColumn('Taxed',           Type.BOOLEAN)
    tableDef.addColumn('Expiration Date', Type.DATE)

    # Column with non-default collation
    tableDef.addColumnWithCollation('Produkt', Type.CHAR_STRING, Collation.DE)

    return tableDef

# Print a Table's schema to stderr.
def printTableDefinition(tableDef):
    for i in range(tableDef.getColumnCount()):
        type = tableDef.getColumnType(i)
        name = tableDef.getColumnName(i)
        print >> sys.stderr, "Column {0}: {1} ({2:#06x})".format(i, name, type)

# Insert a few rows of data.
def insertData(table):
    tableDef = table.getTableDefinition()

    row = Row(tableDef)
    row.setDateTime(0, 2012, 7, 3, 11, 40, 12, 4550) # Purchased
    row.setCharString(1, 'Beans')                    # Product
    row.setString(    2, u'uniBeans'   )             # uProduct
    row.setDouble(    3, 1.08)                       # Price
    row.setDate(      6, 2029, 1, 1)                 # Expiration date
    row.setCharString(7, 'Bohnen')

    for i in range(10):
        row.setBoolean(5, i % 2 == 1)                # Taxed
        row.setInteger(4, i * 10)                    # Quantity
        table.insert(row)

try:
    with Extract('order-py.tde') as extract:

        table = None
        if not extract.hasTable('Extract'):
            # Table does not exist; create it
            tableDef = makeTableDefinition()
            table = extract.addTable('Extract', tableDef)
        else:
            # Open an existing table to add more rows
            table = extract.openTable('Extract')

        tableDef = table.getTableDefinition()
        printTableDefinition(tableDef)

        insertData(table)

except TableauException, e:
    print 'Something bad happened:', e

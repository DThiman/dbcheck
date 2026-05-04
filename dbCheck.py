import pyodbc
import os

username = os.getenv("username")
password = os.getenv("password")


FlowString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=OvakoFlowDB;Trusted_Connection=yes;Encrypt=no"

BluebookString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=BluebookDB;Trusted_Connection=yes;Encrypt=no"

QuotationString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=OvakoQuotationDB;Trusted_Connection=yes;Encrypt=no"


def Check_Database(connectionString):
    ignoreTables=("__MigrationHistory",)
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    cur.execute("SELECT Name from sys.tables;")
    listOfTables = cur.fetchall()
    print(listOfTables)

    for item in listOfTables:
        print(item[0], type(item))

    conn.close()


def getListOfColumnNamesPerTable(tableName, connectionString):
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    cur.execute("SELECT * FROM {table_name};".format(table_name=tableName))
    val = cur.fetchall()

    tableColumns = cur.description
    for item in tableColumns:
        print("column Name: ", item[0], "Column type: ", item[1])
    conn.close()


def removeMigrationHistory(tableNames: list):
    listToReturn = []
    for item in tableNames:
        if item[0] != "__MigrationHistory":
            listToReturn.append(item[0])

    listToReturn.sort()
    return listToReturn


def getListOfTableNames(ConnectionString: str):
    conn = pyodbc.connect(ConnectionString)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sys.tables;")
    tables = cur.fetchall()
    conn.close()
    tab = removeMigrationHistory(tables)

    for item in tab:
        print("Tablename??: ", item)
        getListOfColumnNamesPerTable(item, ConnectionString)
    # return removeMigrationHistory(tables)

getListOfTableNames(QuotationString)
# print(getListOfTableNames(QuotationString))
# conn = pyodbc.connect(QuotationString)
# cur = conn.cursor()
# cur.execute(f"SELECT * FROM QuotationRow;")
# val = cur.fetchall()
# tableColumns = cur.description
# for item in tableColumns:
#     print(item)
# conn.close()

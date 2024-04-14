import pyodbc

class Connection:
    def GetConnectionString():
        driver = "{SQL Server Native Client 11.0}"
        server_name = "DESKTOP-49PGK7I"
        database = "CricketDB"
        sql_user = "sa"
        sql_pass = "sa@2019"
        conn ="Driver="+driver + ";SERVER="+server_name+ ";DATABASE="+database+ ";UID="+sql_user+ ";PWD="+sql_pass
        return conn
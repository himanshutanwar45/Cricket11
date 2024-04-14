import pyodbc
from Classes.Connection.Connection import Connection

class GetMatchList:
    def GetMatchType():
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())
            cursor = conn.cursor()
            cursor.execute("SELECT Match_Type FROM Get_Match_List GROUP BY Match_Type")
            data = cursor.fetchall()
            data_list = []
            for rows in data:
                data_dict = {
                    'Match_Type':rows[0]
                }
                data_list.append(data_dict)
            return data_list 
        except Exception as ex:
            data_list = []
            data_dict = {
                'Match_Type':str(ex)
            }
            data_list.append(data_dict)
            return data_list
        

    def GetRecentmatchList(matchType):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())
            cursor = conn.cursor()
            cursor.execute("EXEC Sp_GetMatchList ?",(matchType))
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for rows in data:
                data_dict = dict(zip(column_names, rows))
                data_list.append(data_dict)
            return data_list
        except Exception as ex:
            data_list = []
            data_dict = {
                'Match_Type':str(ex)
            }
            data_list.append(data_dict)
            return data_list
        

    def GetMatchListScore(matchId):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())
            cursor = conn.cursor()
            cursor.execute("EXEC Sp_Get_MatchHeader ?",(matchId))
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for rows in data:
                data_dict = dict(zip(column_names, rows))
                data_list.append(data_dict)
            return data_list
        except Exception as ex:
            data_list = []
            data_dict = {
                'Match_Id':str(ex)
            }
            data_list.append(data_dict)
            return data_list
        

    def GetBatterDetails(Match_Id,team_id):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())
            cursor = conn.cursor()
            cursor.execute("EXEC Sp_GetBatter_Details ?,?", (Match_Id,team_id))
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for rows in data:
                data_dict = dict(zip(column_names, rows))
                data_list.append(data_dict)
            return data_list
        except Exception as ex:
            return str(ex)
    
    def GetBowlerDetails(Match_Id,team_id):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())
            cursor = conn.cursor()
            cursor.execute("EXEC Sp_GetBowler_Details ?,?", (Match_Id,team_id))
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for rows in data:
                data_dict = dict(zip(column_names, rows))
                data_list.append(data_dict)
            return data_list
        except Exception as ex:
            return str(ex)
            

    
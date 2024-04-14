import pyodbc
from Classes.Connection.Connection import Connection


class GetTeam:
    def GetTeamDetails(teamType):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())
            cursor = conn.cursor()
            cursor.execute("EXEC Sp_GetColumn ? ",(teamType))
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for rows in data:
                data_dict = dict(zip(column_names, rows))
                data_list.append(data_dict)
            return data_list
        except Exception as ex:
            return str(ex)
        
    def GetTeamPlayerDetails(teamId):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())
            cursor = conn.cursor()
            cursor.execute("EXEC Sp_Get_Player_List ?",teamId)
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for rows in data:
                data_dict = dict(zip(column_names, rows))
                data_list.append(data_dict)
            return data_list
        except Exception as ex:
            return str(ex)
        

    def GetTeamPlayerInfo(playerId,teamId):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())
            cursor = conn.cursor()
            cursor.execute("EXEC SP_Get_Player_Info ?,?",playerId,teamId)
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for rows in data:
                data_dict = dict(zip(column_names, rows))
                data_list.append(data_dict)
            return data_list
        except Exception as ex:
            return str(ex)
        

    def GetTeamName(teamId):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Get_Teams WHERE Team_Id = ?",teamId)
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for rows in data:
                data_dict = dict(zip(column_names, rows))
                data_list.append(data_dict)
            return data_list
        except Exception as ex:
            return str(ex)
        

    def GetPlayerName(playerName,teamId):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Get_Players WHERE Player_Id = ? and Team_Id = ?",playerName,teamId)
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for rows in data:
                data_dict = dict(zip(column_names, rows))
                data_list.append(data_dict)
            return data_list
        except Exception as ex:
            return str(ex)
    
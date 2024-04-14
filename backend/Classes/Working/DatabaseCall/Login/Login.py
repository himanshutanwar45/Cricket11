
import pyodbc,uuid
from Classes.Connection.Connection import Connection

class LoginDetails:
    def LoginUser(json_string):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())  
            cursor = conn.cursor()
            cursor.execute("EXEC Sp_Get_Login ?", json_string)
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for row in data:
                data_dict = dict(zip(column_names, row))
                data_list.append(data_dict)
            auth_token = ""
            if len(data_list) > 0:
                auth_token = str(uuid.uuid4())
                #Id = data_list[0].get('User_Code')  
            return auth_token, data_list
        except Exception as ex:
            return str(ex)
        

    def LoginDetails(user_code):
        try:
            conn = pyodbc.connect(Connection.GetConnectionString())  
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Login_Details WHERE User_Code = ?", user_code)
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data_list = []
            for row in data:
                data_dict = dict(zip(column_names, row))
                data_list.append(data_dict)

            return data_list
        except Exception as ex:
            return str(ex)
import pyodbc
import os
import requests
import json
from Classes.Connection.Connection import Connection
from dotenv import load_dotenv


class APIMatchListModule:
    
    load_dotenv()

    def GetMatchListAPI():
        conn = pyodbc.connect(Connection.GetConnectionString())

        url=f"https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

        headers = {
                "X-RapidAPI-Key": os.getenv("API_KEY"),
                "X-RapidAPI-Host": os.getenv("API_HOST")
            }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open('TeamList.json','w') as file:
                json_data = json.dump(response.json(),file,indent=4)
            
            json_string = json.dumps(response.json())

            return  json_string
    
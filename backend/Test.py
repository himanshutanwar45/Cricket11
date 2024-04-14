import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()


url = f"https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
     "X-RapidAPI-Key": os.getenv("API_KEY"),
     "X-RapidAPI-Host": os.getenv("API_HOST")
     }

response = requests.get(url, headers=headers)

if response.status_code == 200:
        with open('TeamList.json', 'w') as file:
            json_data = json.dump(response.json(), file, indent=4)

        json_string = json.dumps(response.json())

        print(json_string)

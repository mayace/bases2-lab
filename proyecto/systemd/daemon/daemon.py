import requests
from os import environ
from dotenv import load_dotenv
import time


load_dotenv()

url = environ.get("UPDATES_URL")
seconds = int(environ.get("UPDATES_SECONDS", 15 * 60))

while True:
    try:
        print(url, seconds)
        body = requests.get(url).content
        print(body)
    except:
        print("Error en conexion")
    time.sleep(seconds)

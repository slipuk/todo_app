# first layer of todo list app, the base that get base dir, database path and connects to it

import sqlite3
from pathlib import Path
import os

# allows to get base dir
BASE_DIR = Path(__file__).resolve().parent.parent

# gets database path
if not os.path.exists(f"{BASE_DIR}/data"):
    os.makedirs(f"{BASE_DIR}/data")
    print("Folder created successfully.")
else:
    print("Folder already exists.")

if not os.path.exists(f"{BASE_DIR}/data/todo.db"):
    with open(f"{BASE_DIR}/data/todo.db", "w") as file:
        file.write("")
    print("File created successfully.")
else:
    print("File already exists")

DATABASE_PATH = BASE_DIR / "data" / "todo.db"


# connects with the database by path
def get_connection():
    return sqlite3.connect(DATABASE_PATH)

#first layer of todo list app, the base that get base dir, database path and connects to it

import sqlite3
from pathlib import Path

#allows to get base dir
BASE_DIR = Path(__file__).resolve().parent.parent

#gets database path
DATABASE_PATH = BASE_DIR / "data" / "todo.db"

#connects with the database by path 
def get_connection():
	return sqlite3.connect(DATABASE_PATH)
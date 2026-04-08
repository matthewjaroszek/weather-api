import os
import sqlite3 as sql
from flask import Flask, jsonify, request
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.getenv("DB_NAME")
DB_NAME = "recent_capitol_final.db"
DB_PATH = BASE_DIR / DB_NAME
HOST = "0.0.0.0"
PORT = 5000
DEBUG = True
APP = 'weather-api'

print(DB_PATH)
conn = sql.connect(DB_PATH)
x = conn.cursor()
    
def get_tables():
    x.execute(f'SELECT name FROM sqlite_master WHERE type=\'table\' AND name NOT LIKE \'sqlite_%\'')






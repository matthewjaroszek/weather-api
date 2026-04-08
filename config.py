import os
import sqlite3 as sql
from flask import Flask, jsonify, request
from pathlib import Path

BASE_DIR = Path('/Users/matthewjaroszek/weather-api').resolve()
DB_NAME = "recent_capitol_final.db"
DB_PATH = BASE_DIR / DB_NAME
HOST = "0.0.0.0"
PORT = 5000
DEBUG = True
APP = 'weather-api'

conn = sql.connect(DB_PATH)
x = conn.cursor()
    
def get_tables():
    x.execute(f'SELECT name FROM sqlite_master WHERE type=\'table\' AND name NOT LIKE \'sqlite_%\'')






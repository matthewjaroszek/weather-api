import os
import sqlite3 as sql
from flask import Flask, jsonify, request
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.getenv("BASE_DIR")
BASE_DIR = Path(BASE_DIR).resolve()
DB_NAME = "recent_capitol_final.db"
DB_PATH = BASE_DIR / DB_NAME
HOST = "0.0.0.0"
PORT = 5000
APP = 'weather-api'

def connect():
    conn = sql.connect(DB_PATH)
    x = conn.cursor()
    return x, conn
    
def get_tables(x):
    x.execute(f'SELECT name FROM sqlite_master WHERE type=\'table\' AND name NOT LIKE \'sqlite_%\'')

def get_pragma(x, table):
    x.execute(f'PRAGMA table_info({table})')

def get_pragmas(x):
    ret = []
    get_tables(x)
    for table in x.fetchall():
        r1 = []
        table = table[0]
        r1.append(f'Table Name: {table}')
        get_pragma(x, table)
        z = x.fetchall()
        for col in z:
            r1.append(col[1])
        ret.append(r1)
    return ret

def ret(data):
    
    # String
    if isinstance(data, str):
        return data
    
    # 1D list/tuple
    if isinstance(data, (list, tuple)) and not isinstance(data, (dict, set)):
        return '\n'.join(map(str, data))
    
    # 2D list/tuple
    if isinstance(data, (list, tuple)):
        rows = []
        for row in data:
            if isinstance(row, (list, tuple)):
                rows.append(' '.join(map(str, row)))
            else:
                rows.append(str(row))
        return '\n'.join(rows)
    
    # Dict
    if isinstance(data, dict):
        items = []
        for k, v in data.items():
            items.append(f"{k}: {v}")
        return '\n'.join(items)
    
    # Anything else
    return str(data)

import os
import sqlite3 as sql
from flask import Flask, jsonify, request
from pathlib import Path
from dotenv import load_dotenv
import shutil
load_dotenv()

BASE_DIR = os.getenv("BASE_DIR")
PORT = os.getenv("PORT")
BASE_DIR = Path(BASE_DIR).resolve()
DB_NAME = "recent_capitol_final.db"
DB_PATH = BASE_DIR / DB_NAME
DB_SOURCE = BASE_DIR / 'source.db'
HOST = "0.0.0.0"
APP = 'weather-api'

shutil.copy(DB_SOURCE, DB_PATH)

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
        r1.append(f'{table}')
        get_pragma(x, table)
        z = x.fetchall()
        for col in z:
            r1.append(col[1])
        ret.append(r1)
    return ret

def ret(data, top_level=True, pre_wrap=True):
    if pre_wrap:
        return f"<pre>{ret(data, top_level, False)}</pre>"
    
    if isinstance(data, str):
        return data

    if not isinstance(data, (list, tuple)):
        return str(data)

    lines = []

    for i, item in enumerate(data):
        if isinstance(item, (list, tuple)) and len(item) == 1:
            item = item[0]

        if isinstance(item, (list, tuple)):
            if all(isinstance(x, str) for x in item): lines.append(", ".join(str(x) for x in item))
            else: lines.append(ret(item, top_level=False, pre_wrap=False))
        else:
            lines.append(str(item))

        if top_level and i < len(data) - 1:
            next_item = data[i + 1]
            if isinstance(next_item, (list, tuple)) and len(next_item) == 1:
                next_item = next_item[0]

            if isinstance(item, (list, tuple)) or isinstance(next_item, (list, tuple)):
                lines.append("")

    return ", ".join(lines)
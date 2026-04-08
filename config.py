import os
import sqlite3 as sql
from flask import Flask, jsonify, request
from pathlib import Path

sql_url = os.getenv('sql_url')
db = 'recent_capitol_final.db'

def connect_sqlite(file_name):
    conn = sql.connect(f'dbs/{file_name}.db')
    x = conn.cursor()
    return x, conn


import pandas as pd
from dotenv import load_dotenv
import os
import sqlite3 as sql
import psycopg2 as pgs
import sys, argparse
from flask import Flask, jsonify, request

load_dotenv()
sql_url = os.getenv('sql_url')
db = 'recent_capitol_final.db'

def connect_sqlite(file_name):
    conn = sql.connect(f'dbs/{file_name}.db')
    x = conn.cursor()
    return x, conn


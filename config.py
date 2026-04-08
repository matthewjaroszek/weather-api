import pandas as pd
from dotenv import load_dotenv
import os
import sqlite3 as sql
import psycopg2 as pgs
import sys, argparse
from flask import Flask, jsonify, request

load_dotenv()
sql_url = os.getenv('sql_url')

def copy_gz(original_name, copy_name):
    copy = pd.read_csv(f'./gzs/{original_name}.gz')
    copy.to_csv(f'./gzs/{copy_name}.gz', index = False)

def get_df(file_name):
    return pd.read_csv(f'./gzs/{file_name}.gz')
    
def summarize_df(df, rows = 0):
    cols = df.columns
    x = 0
    for col in cols:
        x += 1
        print(f'{col:^50}', end = "")
        if x >= 3:
            print("")
            x = 0
        else:
            print(" - ", end = "")
    if (x != 0): print('')
    print('\b\b  ')
    if rows > 0 and rows <= len(df): print("\n", df.head(rows), "\n")
    else: print("")

def summarize_db(conn, rows = 0):
    tables = pd.read_sql_query('SELECT name FROM sqlite_master WHERE type="table"', conn)['name']

    for table in tables:
        #print(f"=== {table} ===")
        if rows >= 0:
            df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT {rows};", conn)
            summarize_df(df, rows)

def rename_col(df, old, new):
    df.rename(columns={old: new}, inplace = True)

def delete_col(df, col):
    df.drop(col, axis = 1, inplace = True)

def connect_sqlite(file_name):
    conn = sql.connect(f'dbs/{file_name}.db')
    x = conn.cursor()
    return x, conn

def check_args(i):
    return len(sys.argv) > i and (int)(sys.argv[i]) == 1

def load_db(df, file_name):
    x, conn = connect_sqlite(file_name)
    df.to_sql(file_name, conn, if_exists='replace', index = False)
    conn.commit()
    conn.close()

def rename_update(file_name, old, new):
    df = get_df(file_name)
    rename_col(df, old, new)
    df.to_csv(f'gzs/{file_name}.gz', index = False)

def delete_update(file_name, col):
    df = get_df(file_name)
    delete_col(df, col)
    df.to_csv(f'gzs/{file_name}.gz', index = False)

def cut_df(df, cols):
    return df[cols]

def clear_db(x):
    x.execute(f'SELECT name FROM sqlite_master WHERE type=\'table\' AND name NOT LIKE \'sqlite_%\'')
    for table in x.fetchall():
        x.execute(f'DELETE FROM {table[0]}')

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

def load_sql(df, table):
    pass 



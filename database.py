import sqlite3
import datetime

DB_NAME = 'production_issues.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS issues 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  timestamp TEXT, line TEXT, machine TEXT, 
                  type TEXT, description TEXT)''')
    conn.commit()
    conn.close()

def insert_issue(line, machine, issue_type, description):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO issues (timestamp, line, machine, type, description) VALUES (?,?,?,?,?)",
              (now, line, machine, issue_type, description))
    conn.commit()
    conn.close()

def get_all_issues():
    import pandas as pd
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM issues", conn)
    conn.close()
    return df
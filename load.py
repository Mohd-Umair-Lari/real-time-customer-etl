# load.py
import sqlite3

def load_data(df, db_name="database.db"):
    conn=sqlite3.connect(db_name)
    df.to_sql('products', conn, if_exists='replace', index=False)
    conn.close()

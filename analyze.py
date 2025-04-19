# analyze.py
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(db_name="database.db"):
    conn=sqlite3.connect(db_name)
    df=pd.read_sql("SELECT * FROM products", conn)
    conn.close()
    
    df['price'].plot(kind='hist', bins=10, title='Price Distribution')
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

if __name__=="__main__":
    analyze_data()

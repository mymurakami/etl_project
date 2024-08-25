# scripts/load.py

import sqlite3
import json

def load(data, db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS apis
                 (API TEXT, Description TEXT, Link TEXT, Category TEXT)''')

    for entry in data:
        c.execute("INSERT INTO apis (API, Description, Link, Category) VALUES (?, ?, ?, ?)",
                  (entry['API'], entry['Description'], entry['Link'], entry['Category']))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    with open("../data/transformed_data.json", "r") as f:
        data = json.load(f)
    load(data, "../data/database.db")
    print("Data loaded successfully into the database.")

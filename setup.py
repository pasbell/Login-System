import os
import sqlite3
import json


    
def create_db(DB_NAME):
    if os.path.isfile(DB_NAME):
        while True:
            overwrite = input("Database file %s already exists. Would you like to overwrite it? [y/n]" % DB_NAME)

            if overwrite == "y":
                print("OK. Overwriting.")
                os.remove(DB_NAME)
                break
            elif overwrite == "n":
                print("OK. Exiting.")
                exit(0)
            else:
                print("Invalid Input")

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE users (
            username VARCHAR,
            password_hash VARCHAR
        )
    """)

    conn.commit()

    print("Database created!")



if __name__ == "__main__":
    with open('config.json') as f:
            configs = json.load(f)
    DB_NAME = configs['DATABASE_NAME']
    create_db(DB_NAME)
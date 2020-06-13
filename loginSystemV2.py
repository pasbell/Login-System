import hashlib
import json
import sqlite3

class LoginSystem: 
    def __init__(self, db_name):   
        self.db_name = db_name


    def isValidLogin(self,username, password):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        m = hashlib.sha256()
        m.update(password.encode())
        password_hash = m.hexdigest()


        res = c.execute("""
                    SELECT *
                    FROM users
                    WHERE
                    username = ? AND
                    password_hash = ?
                    """, (username, password_hash)).fetchone()

        return res is not None

    def is_username_available(self, username):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        res = c.execute("""
            SELECT *
            FROM users
            WHERE
            username = ?
        """, (username,)).fetchone()

        return res is None


    def addUser(self, username, password):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        if(self.is_username_available(username)):
            password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

            c.execute("""
                INSERT INTO
                    users (username, password_hash)
                VALUES
                    (?, ?)
            """, (username, password_hash))

            conn.commit()


if __name__ == '__main__':
    with open('config.json') as f:
            configs = json.load(f)

    l = LoginSystem(configs['DATABASE_NAME'])
    
    l.addUser("Test","Password")
    print(l.isValidLogin("Test", "Password"))
    print(l.isValidLogin("Test", "Passwor1d"))

    

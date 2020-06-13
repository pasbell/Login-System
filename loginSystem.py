import hashlib
import json

class LoginSystem: 
    def __init__(self, config_file = "config.json"):   
        self.credentials = dict()
        self.config_file = config_file
        self.load_credentials(config_file)


    def load_credentials(self, config_file):
        with open(config_file) as f:
            self.credentials = json.load(f)


    def isValidLogin(self,username, password):
        m = hashlib.sha256()
        m.update(password.encode())
        if(self.credentials.get(username) == m.hexdigest()):
            print("This is a secret")
            return True

        else:
            print("Your username or password is incorrect")
            return False

    def addUser(self,username, password):
        if (self.credentials.get(username) is None):
            m = hashlib.sha256()
            m.update(password.encode())
            x = m.hexdigest()
            self.credentials[username] = m.hexdigest()

            with open(self.config_file, "r+") as f:
                data = json.load(f)
                data.update(self.credentials)
                f.seek(0)
                json.dump(data, f)

        else:
            print("Username already exists")

if __name__ == '__main__':
    l = LoginSystem()
    
    l.addUser("Test","Password")
    print(l.isValidLogin("Test", "Password"))
    print(l.isValidLogin("Test", "Passwor1d"))

    

import json
import os

DATA_FILE = "D:\py_training\python-training\day20 - 16-04\bank-application\bank\data\accounts.json"

class FileStore:
    
    def __init__(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'w') as f:
                json.dump([], f)

    def load_accounts(self):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)

    def save_accounts(self, accounts):
        with open(DATA_FILE, 'w') as f:
            json.dump(accounts, f, indent=4)
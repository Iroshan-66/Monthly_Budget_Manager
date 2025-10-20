import sqlite3
import hashlib
import os
from cryptography.fernet import Fernet
import logging
from getpass import getpass

#---------setup logging---------
logging.basicConfig(
    filename="budget_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"

)

#----------encrypton key------------
#here creating a file for create a encryption key

KEY_FILE = "secret.key"
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE,"wb") as kf:
        kf.write(key)
else:
    with open(KEY_FILE,"rb") as kf:
        key=kf.read()

cipher = Fernet(key)

#------------This is for database setup------------




import sqlite3
import hashlib
import os
from cryptography.fernet import fernet
import logging
from getpass import getpass

#---------setup logging---------#
logging.basicConfig(
    filename="budget_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"

)

#----------encrypton key------------#
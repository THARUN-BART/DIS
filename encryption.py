import sqlite3
from cryptography.fernet import Fernet

f = Fernet(Fernet.generate_key())
db = sqlite3.connect(":memory:")

# Setup table and insert encrypted bytes directly (no extra .decode() needed)
db.execute("CREATE TABLE users(name, pwd)")
db.execute("INSERT INTO users VALUES (?, ?)", ("admin", f.encrypt(b"my_secret_pwd")))

# Retrieve and decrypt
row = db.execute("SELECT pwd FROM users WHERE name=?", ("admin",)).fetchone()
print(f.decrypt(row[0]).decode())
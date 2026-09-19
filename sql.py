import sqlite3

db = sqlite3.connect(":memory:")
c = db.cursor()

c.execute("CREATE TABLE users (username TEXT, password TEXT)")
c.execute("INSERT INTO users VALUES ('admin', 'admin123')")

u = "admin'--"
p = "wrong_password"

query = f"SELECT * FROM users WHERE username='{u}' AND password='{p}'"
c.execute(query)

print("Logged in!" if c.fetchone() else "Login failed.")
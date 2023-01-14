import sqlite3

conn = sqlite3.connect('bazadannyh.db')

conn.execute("""
CREATE TABLE IF NOT EXISTS users(
userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name TEXT);
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS actions(
userid INT,
action_type INT);
""")

conn.execute("""
INSERT INTO users(name) VALUES("jhlgyuhk");
""")

conn.commit()

execute = conn.execute("""
    SELECT * FROM users;
    """).fetchall()

print(execute)

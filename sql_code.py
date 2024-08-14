import sqlite3

conn = sqlite3.connect('splitwise.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL)''')

cur.execute('''CREATE TABLE IF NOT EXISTS groups
               (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                members TEXT NOT NULL)''')

cur.execute('''SELECT COUNT(id) FROM users''')

users_count = cur.fetchone()

for user_id in range(1, users_count[0]+1):
    cur.execute(f'''CREATE TABLE IF NOT EXISTS friends_{user_id}
                    (friend_id INTEGER PRIMARY KEY,
                     amount_owed REAL NOT NULL,
                     FOREIGN KEY (friend_id) REFERENCES users(id))''')

    cur.execute(f'''CREATE TABLE IF NOT EXISTS transactions_{user_id}
                    (id INTEGER PRIMARY KEY,
                     transaction_with INTEGER NOT NULL,
                     amount REAL NOT NULL,
                     FOREIGN KEY (transaction_with) REFERENCES users(id))''')

conn.commit()
conn.close()

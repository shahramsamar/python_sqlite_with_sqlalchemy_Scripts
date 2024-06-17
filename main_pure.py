import sqlite3

con = sqlite3.connect("my_database_sqlite.db")
cur = con.cursor()

cur.execute("""Create Table IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL )""")

cur.execute("""CREATE  TABLE IF NOT EXISTS posts(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           title TEXT NOT NULL ,
           description TEXT NPT NULL,
           user_id INTEGER,
           FOREIGN KEY (user_id) REFERENCES users(id) )""")

# cur.execute("INSERT INTO users(username, email, password) VALUES ('shahram','shahramsamar2010@gmail.com','Ss123456')")
# cur.execute("INSERT INTO users(username, email, password) VALUES ('shari','shari@gmail.com','Ss123456')")

# for _ in range(10):
#     cur.execute("INSERT INTO posts(title, description, user_id) VALUES ('book','a book',1)")
# con.commit()

cur.execute("SELECT * FROM users JOIN posts ON users.id=posts.user_id")
data = cur.fetchall()
print(data[0])

cur.execute("SELECT * FROM posts JOIN users ON posts.user_id=users.id")
data = cur.fetchall()
print(data[0])

import sqlite3

db_name = 'db.sqlite'

conn = None
cursor = None

def open():
    global conn, cursor

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def create_tables():
    open()
    cursor.execute('PRAGMA foreign_keys=on')
    do('''CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY,
       login VARCHAR,
       password VARCHAR,
       admin_access VARCHAR)
    ''')
    
    do('''CREATE TABLE IF NOT EXISTS pjs (
       id INTEGER PRIMARY KEY,
       title VARCHAR,
       about VARCHAR,
       img VARCHAR,
       user_id INTEGER,
       FOREIGN KEY (user_id) REFERENCES users (id) 
       )
    ''')
    
    close()

def drop_table():
    open()
    do('DROP TABLE IF EXISTS pjs')
    do('DROP TABLE IF EXISTS users')
    close()

def add_admin():
    open()
    cursor.execute('''INSERT INTO users (login, password, admin_access) VALUES (?, ?, ?)''', ['admin', 'admin', 'True'])
    conn.commit()
    close()

def show_table():
    open()
    cursor.execute('''SELECT * FROM users''')
    print(cursor.fetchall())

    cursor.execute('''SELECT * FROM pjs''')
    print(cursor.fetchall())
    close()

def get_all_users():
    open()
    cursor.execute('''SELECT users.login, users.password FROM users''')
    return cursor.fetchall()

def get_all_logins():
    open()
    cursor.execute('''SELECT users.login FROM users''')
    return cursor.fetchall()

def get_all_passwords():
    open()
    cursor.execute('''SELECT users.password FROM users''')
    return cursor.fetchall()

def get_all_pjs():
    open()
    cursor.execute('''SELECT pjs.id, pjs.title, pjs.about, pjs.img, users.login 
                   FROM pjs INNER JOIN users ON pjs.user_id == users.id''')
    return cursor.fetchall()

def get_pj_by_id(id):
    open()
    cursor.execute('''SELECT pjs.title, pjs.about, pjs.img, users.login
                   FROM pjs INNER JOIN users ON pjs.user_id == users.id WHERE pjs.id == (?)''', [id])
    return cursor.fetchall()
    
def add_pj(title, about, image, user_id):
    open()
    cursor.execute('''INSERT INTO pjs (title, about, img, user_id ) VALUES (?, ?, ?, ?)''', [title, about, image, user_id])
    conn.commit()
    close()

def add_user(login, password):
    admin_access = 'False'
    open()
    cursor.execute('''INSERT INTO users (login, password, admin_access) VALUES (?, ?, ?)''', [login, password, admin_access])
    conn.commit()
    close()

def delete_pj_by_id(id):
    open()
    cursor.execute('''DELETE FROM pjs WHERE pjs.id == (?)''', [id])
    conn.commit()
    close()

def get_all_title():
    open()
    cursor.execute('''SELECT pjs.id, pjs.title FROM pjs''')
    conn.commit()
    titles = cursor.fetchall()
    close()
    return titles

#drop_table()

#create_tables()
   
show_table()

#data = get_all_pjs()

#print(data)

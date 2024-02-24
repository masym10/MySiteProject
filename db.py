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
       password VARCHAR)
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

def insert_test_data():
    open()
    cursor.execute('''INSERT INTO users (login, password) VALUES (?,?)''', ['admin', 'admin'])
    conn.commit()
    close()

def show_table():
    open()
    cursor.execute('''SELECT * FROM users''')
    print(cursor.fetchall())

    cursor.execute('''SELECT * FROM pjs''')
    print(cursor.fetchall())
    close()

def get_all_pjs():
    open()
    cursor.execute('''SELECT pjs.id, pjs.title, pjs.about, pjs.img, users.login 
                   FROM pjs INNER JOIN users ON pjs.user_id == users.id''')
    return cursor.fetchall()

def get_pj_by_id(id):
    open()
    cursor.execute('''SELECT pjs.title, pjs.about, users.login
                   FROM pjs INNER JOIN users ON pjs.author_id == users.id WHERE pjs.id == (?)''', [id])
    return cursor.fetchall()
    
def add_pj(title, about, image, user_id):
    open()
    cursor.execute('''INSERT INTO pjs (title, about, img, user_id ) VALUES (?, ?, ?, ?)''', [title, about, image, user_id])
    conn.commit()
    close()

drop_table()

create_tables()

insert_test_data()

show_table()

add_pj('Python_first_project', 'This is my start in python devolpend', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png', 1)

pj = get_all_pjs()
print(pj)
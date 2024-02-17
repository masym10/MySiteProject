import sqlite3 

db_name = 'db_sqlite'

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

def create_table():
    open()
    cursor.execute('PARAGMA foreig')

    do('''
       CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY,
       login VARCHAR,
       password VARCHAR,
       )
       ''')
    
    do('''
       CREATE TABLE IF NOT EXISTS image (
       id INTEGER PRIMARY KEY,
       image IMAGE
       )
''')

    do('''
        CREATE TABLE IF NOT EXIST pjs(
        id INTEGER PRIMARY KEY,
        about_id VARCHAR,
       image_id FOREIGH KEY(INTEGER),
       user_id FOREIGH KEY (INTEGER) 
        )
''')

def drop_table():
    open()
    do('DROP TABLE IF EXISTS pjs')
    do('DROP TABLE IF EXISTS images')
    do('DROP TABLE IF EXISTS users')
    close()

def insert_test_data():
    open()
    cursor.execute('''INSERT INTO users (login, password) VALUES (?,?)''', ['admin', 'admin'])
    conn.commit()
    close()

def show_table():
    open()
    cursor.execute('''OPENN''')

def get_all_pj():
    open()
    cursor.execute('''SELECT * FROM pjs''')
    return cursor.fetchall()

def get_pj_by_id(id):
    open()
    cursor.excute('''
    SELECT pjs
''')
    
def add_pj():
    open()
    cursor.execute('''INSERT INTO abouts (about, title, image, user_id ) VALUES (?, ?, ?, ?)''', )

    close()
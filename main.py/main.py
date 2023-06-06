import sqlite3

conn = sqlite3.connect('database_todolist.db')

cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS assignments("
               "id INTEGER PRIMARY KEY,"
               "name TEXT,"
               "class TEXT)"
               "")

#cursor.execute("ALTER TABLE assignments ADD done BOOLEAN")

def new_assignment(name=0, class_name=0, deadline=0, done=False):
    cursor.execute("INSERT INTO assignments (name, class, deadline, done) VALUES (?, ?, ?, ?)", (name, class_name, deadline, done))




conn.commit()
conn.close()
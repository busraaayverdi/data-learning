import sqlite3
import os #operating system

def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db") #connection
    cursor = conn.cursor() #cursor imleci -> veri ekleme okuma gibi imleçler
    return conn, cursor

def main():
    conn, cursor = create_database()

if __name__ == '__main__':
    main()
import sqlite3
import os


def create_database():
    database_path = "students.db"

    if os.path.exists(database_path):
        os.remove(database_path)

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    return conn, cursor


def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE Students (
            id INTEGER PRIMARY KEY,
            name NVARCHAR(100) NOT NULL,
            age INTEGER,
            email VARCHAR(255) UNIQUE,
            city VARCHAR(100)
        )
    """)

    cursor.execute("""
        CREATE TABLE Courses(
            id INTEGER PRIMARY KEY,
            course_name NVARCHAR(100) NOT NULL,
            instructor TEXT,
            credit INTEGER
        )
    """)


def insert_sample_data(cursor):
    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)

    print("Sample data inserted successfully")

def basic_sql_operations(cursor):
    #1) SELECT ALL
    print("----------Select All----------")
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}, City: {row[4]}")

    #2) SELECT Columns
    print("----------Select Columns----------")
    cursor.execute("SELECT name, age FROM Students")
    records = cursor.fetchall()
    print(records)

    # 3) WHERE clause
    print("----------Where Age = 20 ----------")
    cursor.execute("SELECT * FROM Students WHERE age = 20")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 4) WHERE with string
    print("----------Where city = New York ----------")
    cursor.execute("SELECT * FROM Students WHERE city = 'New York'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 5) ORDER BY
    print("----------Order by age ----------")
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 6) LIMIT
    print("----------Limit by 3 ----------")
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall()
    for row in records:
        print(row)

def sql_update_delete_insert_operations(conn, cursor):
    #1) Insert
    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com','Miami')")
    conn.commit()

    #2) UPDATE
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6")
    conn.commit()

    #3) DELETE
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()


def aggregate_functions(cursor):
    #1) Count
    print("----------Aggregate Functions Count----------")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 2) Average
    print("----------Aggregate Functions Average----------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 3) MAX - MIN
    print("----------Aggregate Functions Max-Min----------")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone()
    max_age, min_age = result
    print(max_age)
    print(min_age)

    # 4) GROUP BY
    print("----------Aggregate Functions Group by----------")
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall()
    print(result)


def questions():
    '''
    Basit
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Chicago'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin

    Detaylı
    1) Öğrencileri alphabetic şekilde dizerek getirin
    2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    '''


def answers(cursor):
    # 1) Bütün kursların bilgilerini getirin
    print("----------Select Courses----------")
    cursor.execute("SELECT * FROM Courses")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    print("----------Select Teachers----------")
    cursor.execute("SELECT course_name,instructor FROM Courses")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #3) Sadece 21 yaşındaki öğrencileri getirin
    print("----------Select students age = 21----------")
    cursor.execute("SELECT name,age FROM Students WHERE age = 21")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #4) Sadece Chicago'da yaşayan öğrencileri getirin
    print("----------Select students where city = Chicago----------")
    cursor.execute("SELECT name FROM Students WHERE city = 'Chicago' ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    print("----------Select Dr. Anderson Courses----------")
    cursor.execute("SELECT course_name,instructor FROM Courses WHERE instructor = 'Dr. Anderson'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    print("----------Select students age = 21----------")
    cursor.execute("SELECT name FROM Students WHERE name like 'A%'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #7) Sadece 3 ve üzeri kredi olan dersleri getirin
    print("----------Select credits where > 3----------")
    cursor.execute("SELECT course_name ,credit FROM Courses WHERE credit > 3")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Detaylı
    #1) Öğrencileri alphabetic şekilde dizerek getirin
    print("----------Select All----------")
    cursor.execute("SELECT * FROM Students Order BY name ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    print("----------Select All----------")
    cursor.execute("SELECT * FROM Students where age > 20 Order BY name ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    print("----------Select All or----------")
    cursor.execute("SELECT * FROM Students where city = 'Chicago' or city = 'New York'  ")
    records = cursor.fetchall()
    for row in records:
        print(row)


    #4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    print("----------Select All not----------")
    cursor.execute("SELECT * FROM Students where city IS NOT 'New York'")
    records = cursor.fetchall()
    for row in records:
        print(row)




def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn, cursor)
        aggregate_functions(cursor)
        answers(cursor)

        conn.commit()
        print("Tablolar başarıyla oluşturuldu.")

    except sqlite3.Error as error:
        conn.rollback()
        print("SQLite hatası:", error)

    finally:
        conn.close()

    print("Database path:", os.path.abspath("students.db"))


if __name__ == "__main__":
    main()
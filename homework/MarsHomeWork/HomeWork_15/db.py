import mysql.connector as mysql

'''username = st-onl
password = AVNS_tegPDkI5BlB2lW5eASC
host = db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com
port = 25060
database = st-onl'''

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

# Создали студента
query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = ('Shrek', 'Shrekovich')
cursor.execute(query, values)
shrek_id = cursor.lastrowid

# Добавляем ему книг
query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values = [
    ('Kapate', shrek_id),
    ('Как тусоваться на болоте с ослом', shrek_id)
]
cursor.executemany(query, values)

# Создаем группу
query = "INSERT INTO groups (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('Болото', 'nov_2025', 'never')
cursor.execute(query, values)
group_id = cursor.lastrowid

# Добавляем его в группу
query = 'UPDATE students SET group_id = %s WHERE id = %s'
values = (group_id, shrek_id)
cursor.execute(query, values)

# Создаем учебные предметы
query = 'INSERT INTO subjects (title) VALUES (%s)'
values = ('Плетение из биссера',)
cursor.execute(query, values)
subjects_1_id = cursor.lastrowid

query = 'INSERT INTO subjects (title) VALUES (%s)'
values = ('Как захватить мир лежа на диване',)
cursor.execute(query, values)
subjects_2_id = cursor.lastrowid

# Создаем уроки по предметам
query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
values = ('lesson_1', subjects_1_id)
cursor.execute(query, values)
sub_1_lesson_id_1 = cursor.lastrowid

query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
values = ('lesson_2', subjects_1_id)
cursor.execute(query, values)
sub_1_lesson_id_2 = cursor.lastrowid

query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
values = ('lesson_1', subjects_2_id)
cursor.execute(query, values)
sub_2_lesson_id_1 = cursor.lastrowid

query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
values = ('lesson_2', subjects_2_id)
cursor.execute(query, values)
sub_2_lesson_id_2 = cursor.lastrowid

# Проставляем оценки по предметам
query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
values = [
    (5, sub_1_lesson_id_1, shrek_id),
    (10, sub_1_lesson_id_2, shrek_id),
    (15, sub_2_lesson_id_1, shrek_id),
    (90, sub_2_lesson_id_2, shrek_id)
]
cursor.executemany(query, values)

# Выводим оценки по предметам
query = 'SELECT * FROM marks where student_id = %s'
values = (shrek_id,)
cursor.execute(query, values)
marks_in_student = cursor.fetchall()
print(marks_in_student)

# Выводим книги ученика
query = 'SELECT * FROM books where taken_by_student_id = %s'
values = (shrek_id,)
cursor.execute(query, values)
books_in_student = cursor.fetchall()
print(books_in_student)

# Выводим всю информацию, что связана с учеником
query = '''
SELECT * FROM students s
LEFT JOIN groups g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON l.id = m.lesson_id
LEFT JOIN subjects subj ON subj.id = l.subject_id
WHERE s.id = %s'''
values = (shrek_id,)
cursor.execute(query, values)
all_info_in_student = cursor.fetchall()
print(all_info_in_student)

db.commit()

db.close()

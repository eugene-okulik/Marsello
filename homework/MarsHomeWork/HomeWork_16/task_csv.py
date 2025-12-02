import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv')

missing_records = []

with open(data_file_path, newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        name = row['name']
        second_name = row['second_name']
        group_title = row['group_title']
        book_title = row['book_title']
        subject_title = row['subject_title']
        lesson_title = row['lesson_title']
        mark_value = row['mark_value']

        query = '''
        SELECT 1 FROM students s
        JOIN groups g ON s.group_id = g.id
        JOIN books b ON b.taken_by_student_id = s.id
        JOIN marks m ON m.student_id = s.id
        JOIN lessons l ON l.id = m.lesson_id
        JOIN subjects subj ON subj.id = l.subject_id
        WHERE s.name = %s
        AND s.second_name = %s
        AND g.title = %s
        AND b.title = %s
        AND subj.title = %s
        AND l.title = %s
        AND m.value = %s
        '''
        cursor.execute(query, (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value))
        result = cursor.fetchone()

        if not result:
            missing_records.append(row)

cursor.close()
db.close()

if missing_records:
    print("В базе отсутствуют следующие записи из файла:")
    for _ in missing_records:
        print(_)
else:
    print("Все данные из файла присутствуют в базе.")

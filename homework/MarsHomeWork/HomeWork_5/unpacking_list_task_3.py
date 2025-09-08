students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

number_of_students = ', '.join(students)
listing_lessons = ', '.join(subjects)

print(f'Students {number_of_students} '
      f'study these subjects: {listing_lessons}')

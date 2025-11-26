import datetime
import os

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

list_date_datetime = []
list_date_str = []


def read_file_data():
    with open(data_file_path, encoding='utf-8') as data_file:
        for line in data_file:
            a = line[3:29]
            yield a


for i in read_file_data():
    list_date_str.append(i)


def str_in_data(texts):
    for text in texts:
        text = datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')
        list_date_datetime.append(text)


str_in_data(list_date_str)

final_data_1 = list_date_datetime[0] + datetime.timedelta(days=7)
final_data_2 = datetime.datetime.isoweekday(list_date_datetime[1])
final_data_3 = datetime.datetime.now() - list_date_datetime[2]

print(final_data_1)
print(final_data_2)
print(final_data_3.days)

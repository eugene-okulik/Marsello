result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

list_from_text_result_1 = result_1.split()  # делаем список из строки
number_1 = int(list_from_text_result_1[-1]) + 10  # выполняем сложение
list_from_text_result_1.pop(-1)  # удаляем старое значение
list_from_text_result_1.append(str(number_1))  # подставляем новое
list_from_text_result_1 = ' '.join(
    list_from_text_result_1)  # конвертируем обратно в строку

list_from_text_result_2 = result_2.split()
number_2 = int(list_from_text_result_2[-1]) + 10
list_from_text_result_2.pop(-1)
list_from_text_result_2.append(str(number_2))
list_from_text_result_2 = ' '.join(list_from_text_result_2)

list_from_text_result_3 = result_3.split()
number_3 = int(list_from_text_result_3[-1]) + 10
list_from_text_result_3.pop(-1)
list_from_text_result_3.append(str(number_3))
list_from_text_result_3 = ' '.join(list_from_text_result_3)

print(list_from_text_result_1)
print(list_from_text_result_2)
print(list_from_text_result_3)

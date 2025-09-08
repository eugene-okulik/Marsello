text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'

index_number_1 = text_1.index(':') + 2  # находим локатор отсчета
result_1 = int(text_1[index_number_1:]) + 10  # производим вычисления

index_number_2 = text_2.index(':') + 2
result_2 = int(text_2[index_number_2:]) + 10

index_number_3 = text_3.index(':') + 2
result_3 = int(text_3[index_number_3:]) + 10

print(result_1)
print(result_2)
print(result_3)

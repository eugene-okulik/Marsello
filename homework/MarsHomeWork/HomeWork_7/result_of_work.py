# text_1 = "результат операции: 42"
# text_2 = "результат операции: 54"
# text_3 = "результат работы программы: 209"
# text_4 = "результат: 2"
#
#
# def addition(text):
#     list_text = text.split()
#     number = int(list_text[-1]) + 10
#     list_text.pop(-1)
#     list_text.append(str(number))
#     list_text = ' '.join(list_text)
#     print(list_text)
#
#
# addition(text_1)
# addition(text_2)
# addition(text_3)
# addition(text_4)

texts = {"text_1": "результат операции: 42",
         "text_2": "результат операции: 54",
         "text_3": "результат работы программы: 209",
         "text_4": "результат: 2"}

for key, value in texts.items():
    index_number = value.index(':') + 2
    conclusion = int(value[index_number:]) + 10
    new_text = value[:index_number] + str(conclusion)
    print(new_text)

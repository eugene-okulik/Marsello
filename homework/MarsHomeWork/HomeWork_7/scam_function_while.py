random_number = 1

while True:
    number = input(
        'Добро пожаловать, попробуйте угадать цифру которую я загадал: '
    )
    if int(number) == random_number:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('К сожалению вы не угадали, попробуйте снова')

# Способ номер 2
# random_number = 1
# x = []
#
# while random_number != x:
#     x = input(
#         'Добро пожаловать, попробуйте угадать цифру которую я загадал: '
#     )
#     if int(x) == random_number:
#         print('Поздравляю! Вы угадали!')
#     else:
#         print('К сожалению вы не угадали, попробуйте снова')

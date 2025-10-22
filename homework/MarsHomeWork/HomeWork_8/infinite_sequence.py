import sys

# Увеличиваем предел для преобразования целых чисел в строки
sys.set_int_max_str_digits(1000000)


def fibonacci_numbers():
    first_number = 0
    last_number = 1
    while True:
        yield first_number
        result = first_number + last_number
        first_number = last_number
        last_number = result


# Список позиций, на которых нужно распечатать числа Фибоначчи
positions = [5, 200, 1000, 100000]

# Создаем объект-генератор
fib_gen = fibonacci_numbers()

# Проходим по генератору и распечатываем числа на указанных позициях
for position in positions:
    for i in range(position - 1):
        next(fib_gen)
    fib_number = next(fib_gen)
    print(f"Число Фибоначчи на позиции {position}: {fib_number}")

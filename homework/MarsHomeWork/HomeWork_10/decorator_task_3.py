def main_calc(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first < second:
            operation = "/"
        elif first > second:
            operation = "-"

        return func(first, second, operation)

    return wrapper


@main_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))

result = calc(first, second)
print("Результат:", result)

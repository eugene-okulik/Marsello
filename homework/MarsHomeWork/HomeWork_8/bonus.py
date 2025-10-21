import random

salary = int(input('Введите свою зарплату т.р. '))
bonus = [True, False]


if random.choice(bonus) == True:
    bonuses = random.randrange(10, 31)
    count = salary // 100 * bonuses + salary
    print(f'Прибавка к вашей зп составит {bonuses}%, итого у Вас {count} т.р.')
else:
    print(f'Ваша зп в этом месяце без изменений {salary}')

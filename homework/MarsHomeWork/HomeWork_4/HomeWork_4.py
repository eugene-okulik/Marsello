my_dict = {
    'tuple': (1, 12, None, False, 'нифига себе я питонист'),
    'list': ['i', 'am', 'an', 'automator', 3000],
    'dict': {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
    'set': {'a', 'b', 5, True, 12.5}
}

#  находим нужные нам объекты, заключаем их в переменные
my_dict_tuple = my_dict['tuple']
my_dict_list = my_dict['list']
my_dict_dict = my_dict['dict']
my_dict_set = my_dict['set']

my_dict_list.append(2.5)
my_dict_list.pop(1)

my_dict_dict[('i am a tuple',)] = 'что здесь происходит?:D'
my_dict_dict.pop(1)

my_dict_set.add('d')
my_dict_set.remove('a')

print(my_dict_tuple[-1])
print(my_dict_set)

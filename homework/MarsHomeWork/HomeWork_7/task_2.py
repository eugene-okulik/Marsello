words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, item in words.items():
    result = int(item) * key
    print(result)


# Способ номер 2
def sort(variable):
    for key, item in variable.items():
        result = int(item) * key
        print(result)


sort(words)

text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
        )

text_list = text.split()  # конвертируем в список для работы со словами
final_text = []  # определяем переменную куда будем складывать результат

for word in text_list:

    if ',' in word:
        comma = word.replace(',', 'ing,')
        final_text.append(comma)

    elif '.' in word:
        dot = word.replace(',', 'ing,')
        final_text.append(dot)

    else:
        words = word + 'ing'
        final_text.append(words)

print(' '.join(final_text))  # выводим в читаемом формате

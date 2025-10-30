PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
txt_formating = PRICE_LIST.replace('\n', ' ')
list_from_text = txt_formating.split()

new_dict = {
    list_from_text[i]: int(list_from_text[i + 1].replace('р', ''))
    for i in range(0, len(list_from_text), 2)
}

print(new_dict)

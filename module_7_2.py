# Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта. Написать усовершенствованную функцию записи.
# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    num_string = 0
    for string in strings:
        num_string += 1
        strings_positions[num_string, file.tell()] = string
        file.write(string + '\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
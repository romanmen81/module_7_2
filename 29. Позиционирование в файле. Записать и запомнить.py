def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            # Запоминаем текущую позицию в файле перед записью
            byte_position = file.tell()
            # Записываем строку в файл, добавляя перевод строки
            file.write(string + '\n')
            # Добавляем информацию в словарь
            strings_positions[(index, byte_position)] = string

    return strings_positions


# Пример выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
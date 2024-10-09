import json
import re


def words_s():
    try:
        with open("text_file.txt", "r", encoding="utf-8") as file1:
            # Читаємо вміст файлу і беремо перше речення (до першої крапки)
            op_f = file1.read().split('.')[0] + '.'
            print("Перше речення: \n", op_f)

            # Видаляємо всі символи пунктуації, крім пробілів
            normal_string = re.sub(r'[^\w\s]', '', op_f)

            # Розбиваємо речення на слова
            words = normal_string.split()

            # Розділяємо українські та англійські слова
            ang_resalt = [word for word in words if re.match(r'[A-Za-z]+', word)]
            uk_resalt = [word for word in words if re.match(r'[А-Яа-яЇїҐґЄєЮю]', word)]

            # Сортуємо слова окремо для українських та англійських
            ang_sort = sorted(ang_resalt, key=str.lower)
            uk_sort = sorted(uk_resalt, key=str.lower)

            # Виводимо відсортовані слова
            print("Українські слова: \n", uk_sort)
            print("Англійські слова: \n", ang_sort)

            return print("Відсортовані слова: \n",uk_sort + ang_sort)  # Повертаємо результат як об'єднаний список
    except Exception as e:
        return f"Error: {str(e)}"

# Викликаємо функцію
words_s()



# Вариант 1. Через функции строки
#
# text = '[1, 2, 3]'
# parse = text.strip('[]').replace(' ', '').split(',')  # список из строковых значений, потом можно преобразовать в нужный формат
# Вариант 2. Через библиотеку json.
#
# import json
# text = '[1, 2, 3]'
# parse = json.loads(text)
# Вариант 3. Парсим через библиотеку re
# parse = re.findall('([-+]?\d+)', text)  # Если в строке-списке будут только целые числа
# parse = re.findall('([-+]?\d*\.\d+|\d+)', text)  # Если будут е
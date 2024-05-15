# 15)Подсчет количества слов в файле:
#    Создайте программу, которая подсчитывает количество слов в текстовом файле и выводит это число.
# 16)Запись в файл:   Попросите пользователя ввести некоторый текст и сохраните его в текстовом файле.
# 17)Копирование файла:
#    Напишите программу, которая копирует содержимое одного файла в другой файл.

# 1
def words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            return word_count
    except FileNotFoundError:
        print("Файл не найден")
        return -1

filename = input("Введите имя файла: ")
word_count = words(filename)
if word_count != -1:
    print("Количество слов в файле:", word_count)
# 2




# 3
# text = """Lorem"""

# with open("text.txt", "w") as ex2:
#     ex2.write(text)

# ex2 = open("text.txt", "w")
# ex2.write(text)
# ex2.close
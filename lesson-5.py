# 1. Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода
# данных свидетельствует пустая строка."""""


fname = input('Ведите файл: ')
f = open(fname, 'w')
while True:
    s = input()
    if s == '': break
    f.write((s+'\n'))
f.close()


# 2. Создать текстовый файл (не программно), сохранить в нем
# несколько строк, выполнить подсчет количества строк, количества
# слов в каждой строке.

my_file = open('newfile.txt', 'r')
content = my_file.read()
print(content)
my_file = open('newfile.txt', 'r')
content = my_file.read()
print(f'Количество букв - {len(content)}')
my_file = open('newfile.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Количество слов - {len(content)}')
my_file = open('newfile.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'{i + 1}  {len(content[i])}')
my_file.close()

# newfile.txt
# my nuw file
# qwe qwe qwe
# QWE QWE QWE
# uyi uhb uui

# 3. Создать текстовый файл (не программно), построчно записать
# фамилии сотрудников и величину их окладов. Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
# сотрудников. Выполнить подсчет средней величины дохода сотрудников.

fil = {
    'Piter': 17000,
    'Margo': 21000,
    'Renat': 18000,
    'Uliana': 22000,
    'Margo': 16000,
    'Leo': 19000
}
try:
    f_obj = open('newfile.txt', 'w')
    for last_name, salary in fil.items():
        f_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print('Oшибка')
finally:
    f_obj.close()

sal = 0
poor = 0
person = []

with open('newfile.txt', 'r') as f_obj:

    # my_list = f_obj.read().split('\n')
    for line in f_obj:
        print(line, end='')
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
           person.append(tokens[0])
        sal += int(tokens[1])
        poor += 1
res = sal / poor
print(f"persons: {person}")
print(f"averate: {poor}")



# with open('newfile.txt', 'w') as file:
#
# inputfile = "newfile.txt"
# my_file = open(inputfile, mode='r', encoding='ascii')
# print(my_file.read())

# """""4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл."""""

# file = {
#     'One': 'Один',
#     'two': 'Два',
#     'Three':'Три',
#     'Four':'Четыре'
# }
# try:
#     f_obj = open('name.txt', 'r')
#     for last_name, salary in file.items():
#         f_obj.write(last_name + ':' + str(salary) + "\n")
# except IOError:
#     print('Oшибка')
# finally:
#     f_obj.close()

translater = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4}
my_list = []
result = []

int
file_obj = open('name.txt', mode='r', encoding='utf-8')
for line in file_obj:
    tokens = line.split()
    print(tokens)
file_obj.close()

try:
    file_input = open("name1.txt", mode='w', encoding='utf-8')
    file_input.writelines(result)
except IOError:
    print('ошибка!')
finally:
    file_input.close()


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

# with open('input.txt') as t:
#     print (*(sum(map(int, line.splite())) for line in t.readline()) ,sep= '\n')





 #     s = input()
#     if s == '': break
#     f.write((s+'\n'))
# f.close()



fname = input('Ведите файл: ')
f = open(fname, 'w')
while True:
    ex = False
    result = 0
    while ex == False:
        numbers = input('Enter numbers or q to exit: ').split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            else:
                res_line += int(num)
        result += res_line
    print((sum(map(int, result))))
f = open(fname, 'w')
f.close()

fname = input('Ведите файл: ')
f = open(fname, 'w')
while True:
    s = input()
    if s == '': break
    f.write((s+'\n'))
f.close()

# -------------------

import sys


# inp = open('newfile.txt', 'r')
# out = open('newfile.txt', 'a')
# summ = 0
# numbers = inp.read()# читаем файл
# numbers = re.findall(r'[+-]?\d+', numbers) # находим все числа без/с префиксами + и -
# numbers = [int(x) for x in numbers]
# # приводим числа к типу int с помощью list comprehension
# # суммируем числа


# for x in numbers:
#     summ += x
#
# out.write(str(summ))
# # записываем результат, обязательно в виде строки
# # закрываем файлы
# inp.close()
# out.close()

#
#-----------------------
#
# def summary():
#     try:
#         with open('file_5.txt', 'w+') as file_obj:
#             line = input('Введите через пробел \n')
#             file_obj.writelines(line)
#             my_numb = line.split()
#
#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Ошибка')
#     except ValueError:
#         print('Ошибка')
# summary()
#

# 6. Необходимо создать (не программно) текстовый файл, где каждая
# строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему. Вывести
# словарь на экран.
#
# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
#
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}



# subj = {}
# with open('za6.txt', mode='r', encoding='utf-8') as file:
#     for i, in file:
#
#         print(f'{i}')

# -----------------
# za6.txt
# Алгебра 40(пар)
# # Физика 20(пар) 10(лаб)
# # Физкультура 30(пар)

my_f = open("za6.txt", mode='r', encoding='utf-8')
content = my_f.readlines()
print(content)
my_f.close()


# subj = {}
# with open('za6.txt', mode='r', encoding='utf-8') as ini:
#     for line in ini:
#         print(line)

# content = my_file.read()

# print(ini:)






#7. Создать (не программно) текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в
# расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами
# и их прибылями, а также словарь со средней прибылью. Если фирма
# получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

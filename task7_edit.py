# Самостоятельное задание

# Дана строка из двух слов. Поменяйте слова местами.

string = 'test new'

test_list = string.split( )
string_new = str(test_list[1] + ' ' + test_list[0])

print(string_new +'\n')

# Домашнее задание

import calendar

# С помощью модуля calendar узнайте, является ли 2030 год високосным 

leap = calendar.isleap(2030)

if leap == 'True':
    print('2030 год будет викосным')
else:
    print('2030 год НЕ будет викосным\n')
    
# С помощью модуля calendar узнайте, каким днем недели
# был день 25 июня 2000 года.

day = calendar.weekday(2000, 6, 25)

if day == 0:
    print('Понедельник')
elif day == 1:
    print('Вторник')
elif day == 2:
    print('Среда')
elif day == 3:
    print('Четверг')
elif day == 4:
    print('Пятница')
elif day == 5:
    print('Суббота')
else:
    print('Воскресенье')
    
# Выведите в консоль календарь на 2023 год

cal = calendar.TextCalendar()
print(cal.formatyear(2023))

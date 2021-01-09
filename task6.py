# Самостоятельное задание

d = {"NewYork": 'DreamCity'}
d["new_value"] = 754
d[(1, 6, 8, 17, 156, 344)] = [1, 45, 18, 756, 519, 640]
print('\n' + d.get("NewYork"))
del d["new_value"]
print(d.keys(), '\n')

# Домашние задания

# Задание 1

#Необходимо вывести элементы, которые одновременно 1) меньше 30 и
# 2) делятся на 3 без остатка. Все остальные элементы списка необходимо
# просуммировать и вывести конечный результат.

lst = [11, 5, 8, 32, 20, 3, 20, 132, 21, 4, 777, 8, 45]

sum_elem = 0

print('Элементы удовлетворяющие условию:')

for i in lst:
    if i < 30 and i % 3 == 0:
        print(i)
    else:
        sum_elem += i
        
print('\nСумма остальных элкментов:', sum_elem)

# Задание 2

# Написать функцию month_to_s (), которая принимает 1 аргумент
# - номер месяца - и возвращает название сезона, к которому относится
# этот месяц. Например, передаем 2, на выходе получаем 'Зима'.


def month_to_s (month):
    if month <= 2 or month == 12:
       return 'Зима'
    elif month >= 3 and month <= 5:
        return 'Весна'
    elif month >=6 and month <= 8:
        return 'Лето'
    else:
        return 'Осень'

class WrongValueException(Exception):
    pass

try:
    value = int(input('\nВведите число от 1 до 12: '))
    if value <= 0 or value > 12:
        raise WrongValueException("\nВведено невалидное значение: " + str(value)) 
    print('\n' + month_to_s (value))
    
except WrongValueException as e:
    print(e) 


# Задания

# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# 1) Нужно вернуть список, который состоит из элементов, общих для этих
# двух списков.
# 2) Выведите первый и последний элемент списка.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(a[0], a[len(a)-1], b[0], b[len(b)-1])
c = []
for i in a:
    if b.count(i)>0:
        c.append(i)
for i in c:
    if c.count(i)>1:
        c.remove(i)
print(c)

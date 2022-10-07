#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
#исходной последовательности в том же порядке.
from random import randint
list = [randint(1, 10) for i in range(10)]
print(list)
res = []
for i in range(len(list)):
    for j in range(len(list)):
        if i != j and list[i] == list[j]:
            break
    else:
       res.append(list[i])
print(res)
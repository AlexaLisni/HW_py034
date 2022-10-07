#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
#исходной последовательности в том же порядке.
from random import sample


a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')
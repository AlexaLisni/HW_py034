#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
num = int(input())
i = 2
primfac = []
while i * i <= num:
    while n % i == 0:
        primfac.append(i)
        n = n / i
    i = i + 1
if n > 1:
    primfac.append(n)
print(primfac)

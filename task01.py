#1. Вычислить число c заданной точностью d

from decimal import Decimal, ROUND_HALF_DOWN
num = Decimal(input())
d = input()
print(num.quantize(Decimal(d),ROUND_HALF_DOWN)) 
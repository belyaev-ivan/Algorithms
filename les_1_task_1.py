import math

x = int(input('Введите целое число'))
a = math.floor(x/100)
c = x - (math.floor(x/10))*10
b = int((x - a*100 - c)/10)
print(f'Сумма равна {a + b + c}')
print(f'Произведение равно {a * b * c}')

print("Введите три разных числа")
a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
c = int(input('Введите третье число'))

if a > b and c > a and c > b:
    print('Первое число является средним')
elif b > a and c > a and c > b:
    print('Второе число является средним')
elif a > c and b > a and b > c:
    print('Первое число является средним')
elif c > a and c > a and b > c:
    print('Третье число является средним')
elif b > c and a > c and a > b:
    print('Второе число является средним')
elif c > b and a > c and a > b:
    print('Третье число является средним')
else:
    print("Все числа равны")

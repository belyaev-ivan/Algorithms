import random

x = int(input('Введите режим работы программы (1 - нахождение случайного целого числа в заданном диапазоне, '
              '2 - вещественного числа, 3 - символа)'))
b = input('Введите верхнюю границу диапазона')
a = input('Введите нижнюю границу диапазона')
z = 0

if x == 1:
    z = random.randint(int(a), int(b))
    print(z)

else:
    if x == 2:
        z = random.uniform(float(a), float(b))
        print(z)
    else:
        if a == 'a':
            a = 1
        if a == 'b':
            a = 2
        if a == 'c':
            a = 3
        if a == 'd':
            a = 4
        if a == 'e':
            a = 5
        if a == 'f':
            a = 6
        if a == 'g':
            a = 7
        if a == 'h':
            a = 8
        if a == 'i':
            a = 9
        if a == 'j':
            a = 10
        if a == 'k':
            a = 11
        if a == 'l':
            a = 12
        if a == 'm':
            a = 13
        if a == 'n':
            a = 14
        if a == 'o':
            a = 15
        if a == 'p':
            a = 16
        if a == 'q':
            a = 17
        if a == 'r':
            a = 18
        if a == 's':
            a = 19
        if a == 't':
            a = 20
        if a == 'u':
            a = 21
        if a == 'v':
            a = 22
        if a == 'w':
            a = 23
        if a == 'x':
            a = 24
        if a == 'y':
            a = 25
        if a == 'z':
            a = 26

        if b == 'a':
            b = 1
        if b == 'b':
            b = 2
        if b == 'c':
            b = 3
        if b == 'd':
            b = 4
        if b == 'e':
            b = 5
        if b == 'f':
            b = 6
        if b == 'g':
            b = 7
        if b == 'h':
            b = 8
        if b == 'i':
            b = 9
        if b == 'j':
            b = 10
        if b == 'k':
            b = 11
        if b == 'l':
            b = 12
        if b == 'm':
            b = 13
        if b == 'n':
            b = 14
        if b == 'o':
            b = 15
        if b == 'p':
            b = 16
        if b == 'q':
            b = 17
        if b == 'r':
            b = 18
        if b == 's':
            b = 19
        if b == 't':
            b = 20
        if b == 'u':
            b = 21
        if b == 'v':
            b = 22
        if b == 'w':
            b = 23
        if b == 'x':
            b = 24
        if b == 'y':
            b = 25
        if b == 'z':
            b = 26
        z = random.randint(a, b)
        if z == 1:
            print('a')
        if z == 2:
            print('b')
        if z == 3:
            print('c')
        if z == 4:
            print('d')
        if z == 5:
            print('e')
        if z == 6:
            print('f')
        if z == 7:
            print('g')
        if z == 8:
            print('h')
        if z == 9:
            print('i')
        if z == 10:
            print('j')
        if z == 11:
            print('k')
        if z == 12:
            print('l')
        if z == 13:
            print('m')
        if z == 14:
            print('n')
        if z == 15:
            print('o')
        if z == 16:
            print('p')
        if z == 17:
            print('q')
        if z == 18:
            print('r')
        if z == 19:
            print('s')
        if z == 20:
            print('t')
        if z == 21:
            print('u')
        if z == 22:
            print('v')
        if z == 23:
            print('w')
        if z == 24:
            print('x')
        if z == 25:
            print('y')
        if z == 26:
            print('z')


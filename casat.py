import math
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x - math.cos(x)


def g(x):
    return 1 + math.sin(x)


def gg(x):
    return math.cos(x)


def cas(left, right, epsilon):
    i = 0
    if func(left)*gg(left) > 0:
        print('Условие на сходимость выполнено в начале отрезка')
        c = left
    elif func(right)*gg(right) > 0:
        print('Условие на сходимость выполнено в конце отрезка')
        c = right
    else:
        print('Условие на сходимость не выполнено')
        return None
    while abs(func(c)) > epsilon:
        i += 1
        c -= func(c)/g(c)
    print(f'Количество итераций: {i}')
    return c


a = int(input('Введите интервал\n'))
b = int(input())
eps = 0.000001
p = np.arange(-100, 100, 0.01)
ans = cas(a, b, eps)
if ans == None:
    exit(0)
print(f'x={ans}')
plt.plot(p, [func(i) for i in p], 'r')
plt.title('График ф-ции x-cos(x)')
plt.plot(ans, func(ans), 'go')
plt.show()

import math
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x - math.cos(x)


def horda(left, right, epsilon):
    i = 0
    while True:
        i += 1
        c = left - (func(left) / (func(right) - func(left))) * (right - left)
        if func(c) * func(left) > 0:
            left = c
        else:
            right = c
        if abs(func(c)) < epsilon:
            print(f'Количество итераций: {i}')
            return c


a = float(input('Введите интервал\n'))
b = float(input())
while True:
    if func(a)*func(b) >= 0:
        print('На данном отрезке нет решения')
        a = float(input())
        b = float(input())
    else:
        break
eps = 0.0000001
p = np.arange(a, b, 0.01)
ans = horda(a, b, eps)
print(f'x={ans}')
plt.plot(p, [func(i) for i in p], 'r')
plt.title('График ф-ции x-cos(x)')
plt.plot(ans, func(ans), 'go')
plt.show()
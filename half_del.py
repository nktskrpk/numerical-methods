import math
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x - math.cos(x)


def half_del(left, right, epsilon):
    i = 0
    while True:
        if abs(left-right) < epsilon:
            print(f'Количество итераций: {i}')
            return c
        else:
            i += 1
            c = (left + right) / 2
            if func(left) * func(c) < 0:
                right = c
            else:
                left = c


a = float(input('Введите интервал\n'))
b = float(input())
eps = 0.000001
while True:
    if func(a)*func(b) >= 0:
        print('На данном отрезке нет решения')
        a = float(input())
        b = float(input())
    else:
        break
p = np.arange(a, b, 0.01)
ans = half_del(a, b, eps)
print(f'x={ans}')
plt.plot(p, [func(i) for i in p], 'r')
plt.title('График ф-ции x-cos(x)')
plt.plot(ans, func(ans), 'go')
plt.show()

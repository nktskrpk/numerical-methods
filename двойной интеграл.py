from scipy.integrate import dblquad
from numexpr import evaluate


def solve_integral(low_lim, up_lim, low_lim_inside, up_lim_inside, func):
    c1 = lambda x: evaluate(low_lim_inside)
    d1 = lambda x: evaluate(up_lim_inside)
    f1 = lambda x, y: evaluate(func)
    return dblquad(f1, low_lim, up_lim, c1, d1)[0]


if __name__ == '__main__':
    a = int(input('a= '))
    b = int(input('b= '))
    c = input('c= ')
    d = input('d= ')
    f = input('Введите функцию: ')
    print(f'результат: {solve_integral(a, b, c, d, f)}')

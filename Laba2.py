'Вычислить сумму знакопеременного ряда |х(3n-1)|/(3n-1)!, где х-матрица ранга к (к и матрица задаются случайным образом),'
'n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.'
'У алгоритма д.б. линейная сложность. Операция умножения –поэлементная'


import numpy as np
from numpy import linalg

while True:
    sign = int(input('Введите размерность матрицы (от 4 до 15):'))
    if(sign < 4) or (sign > 16):
        print('Вы ввели неправильную размерность!!!')
    else:
        break
array = np.random.randint(100, size=(sign, sign))
print(array)
while True:
    t = int(input('Введите количество знаков после запятой: '))
    if t < 0:
        print('Количество знаков после запятой не должно быть отрицательным')
    else:
        break
t = 0.1**t
n = 1
fac = 2
second = 1
sum = 0
sum_t = 0
while abs(second) > t:
    sum_t += sum
    stepen = 3*n - 1
    sum += (np.linalg.det(linalg.matrix_power(array, stepen))) / fac
    fac *= (n+1) * (n+2) * (n+3)
    n += 1
    second = abs(sum_t-sum)
    sum_t = 0
    print(n-1, ':', sum, '  ', second)
print('Сумма равна: ', sum)
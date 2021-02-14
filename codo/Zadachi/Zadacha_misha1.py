"""Вам даны массивы A и B одинаковой длины N, каждый массив состоит из попарно различных целых
чисел. Требуется переупорядочить элементы массива B так, чтобы для любых двух различных
чисел i и j от 1 до N выполнялось равенство (A[i] − A[j]) ∗ (B[i] − B[j]) > 0.
Input
Первая строка входного файла содержит целое число N (2 ≤ N ≤ 10**5).
Вторая строка содержит N целых чисел — элементы массива A в том порядке, в котором
они заданы в массиве.
Третья строка содержит массив B в аналогичном формате.
Элементы массива — целые числа от −10**9 до 10**9
.
Output
Выведите массив B, упорядоченный в соответствии с требованиями задачи. Если таких
упорядочений несколько, выберите любое."""
# TODO сделать таймер с отсчетом секунд в консоли
from random import randint
from time import time
#N = int(input())
N = 9**5

#A = list(map(int, input().split()))git
A = [randint(-10**9, 10**9) for _ in range(N)]

#B = list(map(int, input().split()))
B = [randint(-10**9, 10**9) for _ in range(N)]
#B = [10, 8, -3, 60, 0, 6]
start = time()
print("Start")
for i in range(0, N):
    for j in range(0, N):
        if i != j and (A[i] - A[j]) * (B[i] - B[j]) <= 0:
            B[i], B[j] = B[j], B[i]

for i in range(0, N):
    for j in range(0, N):
        if i != j and (A[i] - A[j]) * (B[i] - B[j]) <= 0:
            B[i], B[j] = B[j], B[i]
end = time()
print(B)
print(end - start)
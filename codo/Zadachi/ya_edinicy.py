"""
Последовательно идущие единицы
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Требуется найти в бинарном векторе самую длинную
последовательность единиц и вывести её длину.

Желательно получить решение, работающее за линейное
 время и при этом проходящее по входному массиву только один раз.

Формат ввода
Первая строка входного файла содержит одно число n, n ≤ 10000.
 Каждая из следующих n строк содержит ровно одно число
 — очередной элемент массива.

Формат вывода
Выходной файл должен содержать единственное число — длину самой
длинной последовательности единиц во входном массиве.

Пример
5
1
0
1
0
1
Вывод
1

Решеине верное
"""

n = int(input())
A = [int(input()) for i in range(n)]
k = 0
max_k = 0
for i in A:
	if i:
		k += 1
	else:
		if k > max_k:
			max_k = k
		k = 0
if k > max_k:
	max_k = k
print(max_k)
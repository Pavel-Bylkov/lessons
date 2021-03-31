"""
Анаграммы

Ограничение времени	1 секунда
Ограничение памяти	20Mb

Даны две строки, состоящие из строчных латинских букв.
Требуется определить, являются ли эти строки анаграммами,
т. е. отличаются ли они только порядком следования символов.

Формат ввода
Входной файл содержит две строки строчных латинских символов,
каждая не длиннее 100 000 символов. Строки разделяются
символом перевода строки.

Формат вывода
Выходной файл должен содержать единицу, если строки являются
 анаграммами, и ноль в противном случае.

Пример 1
qiu
iuq

Вывод
1

Пример 2
zprl
zprc

Вывод
0

Решение прошло тесты только на Python 3.7.3

"""

a = input()
b = input()
R = {}
for s in a:
	if s in R:
		R[s] += 1
	else:
		R[s] = 1
K = {}
for s in b:
	if s in K:
		K[s] += 1
	else:
		K[s] = 1
if R == K:
	print(1)
else:
	print(0)
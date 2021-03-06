"""
Интересное путешествие

Ограничение времени	1 секунда
Ограничение памяти	64Mb

Не секрет, что некоторые программисты очень любят путешествовать.
Хорошо всем известный программист Петя тоже очень любит путешествовать,
посещать музеи и осматривать достопримечательности других городов.
Для перемещений между из города в город он предпочитает использовать
машину. При этом он заправляется только на станциях в городах, но не
на станциях по пути. Поэтому он очень аккуратно выбирает маршруты,
чтобы машина не заглохла в дороге. А ещё Петя очень важный член команды,
поэтому он не может себе позволить путешествовать слишком долго. Он
решил написать программу, которая поможет ему с выбором очередного
путешествия. Но так как сейчас у него слишком много других задач, он
попросил вас помочь ему.
Расстояние между двумя городами считается как сумма модулей разности
по каждой из координат. Дороги есть между всеми парами городов.

Формат ввода
В первой строке входных данных записано количество городов  n (2≤n≤1000).
В следующих n строках даны два целых числа: координаты каждого города,
не превосходящие по модулю миллиарда. Все города пронумерованы числами
от 1 до n в порядке записи во входных данных.
В следующей строке записано целое положительное число k, не превосходящее
двух миллиардов, — максимальное расстояние между городами, которое Петя
может преодолеть без дозаправки машины.
В последней строке записаны два различных числа — номер города, откуда
едет Петя, и номер города, куда он едет.

Формат вывода
Если существуют пути, удовлетворяющие описанным выше условиям, то выведите
минимальное количество дорог, которое нужно проехать, чтобы попасть из
начальной точки маршрута в конечную. Если пути не существует, выведите -1.

Пример 1
7
0 0
0 2
2 2
0 -2
2 -2
2 -1
2 1
2
1 3

Вывод
2

Пример 2
4
0 0
1 0
0 1
1 1
2
1 4

Вывод
1

Пример 3
4
0 0
2 0
0 2
2 2
1
1 4

Вывод
-1


"""
from itertools import combinations, product

n = int(input())
cities = {i: tuple(map(int, input().split())) for i in range(1, n + 1)}
k = int(input())
c_from, c_to = tuple(map(int, input().split()))
n = 1
S = {(x, s) for x in cities for s in cities if x != s}
S = {city for city in S if abs(cities[city[0]][0] - cities[city[1]][0]) +
     abs(cities[city[0]][1] - cities[city[1]][1]) <= k}

def intersection(S_from, S_to, deep=2):
    if c_to in S_from or c_from in S_to:
        return deep
    if
    S_from = {s[1] for s in S if s[0] in S_from}
    S_to = {s[1] for s in S if s[0] in S_to}
    return intersection(S_from, S_to, deep + 1)

if len(S) == 0:
    print(-1)
elif (c_from, c_to) in S:
    print(1)
else:
    S_from = {s[0] for s in S if s[0] == c_from}
    S_to = {s[0] for s in S if s[0] == c_to}
    print(intersection(S_from, S_to))

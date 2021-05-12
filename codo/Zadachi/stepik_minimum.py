"""
На обработку поступает последовательность из 1010 целых чисел.
Известно, что вводимые числа по абсолютной величине не превышают 10^6.
Нужно написать программу, которая выводит на экран сумму всех отрицательных
чисел последовательности и максимальное отрицательное число в последовательности.
Если отрицательных чисел нет, требуется вывести на экран «NO». Программист
торопился и написал программу неправильно.

Найдите все ошибки в этой программе (их ровно 55). Известно, что каждая
ошибка затрагивает только одну строку и может быть исправлена без изменения
других строк.

Примечание 1. Число xx не превышает по абсолютной величине 10^6, если -10^6 ≤ x ≤ 10^6.

Примечание 2. При необходимости вы можете добавить необходимые строки кода.
"""

mx = -10**7
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        if x > mx:
            mx = x
if s == 0:
    print("NO")
else:
    print(s)
    print(mx)

s = 'i Learn Python language'
print(s.capitalize())


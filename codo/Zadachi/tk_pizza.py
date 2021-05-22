from time import time as t
from random import randint
# n, m = (int(i) for i in input().split())
# time = [int(i) for i in input().split()]
n, m = 20000, 10**5
time = [randint(5, 500) for _ in range(m)]
start = t()
flags = [False] * m
current_time = min(time)
while n > 0:
    for i in range(m):
        if current_time % time[i] == 0:
            if not flags[i]:
                n -= 1
                flags[i] = True
            else:
                flags[i] = False
            if n == 0:
                break
    current_time += 1
print(current_time - 1, t() - start)

# from random import randint
# from time import time as t
# class User:
#     def __init__(self, time: str):
#         self.time = int(time)
#         self.current_time = self.time
#     def next(self):
#         self.current_time += 2 * self.time
#     def __lt__(self, other): # x < y
#         return self.current_time < other.current_time
#
#
# n, m = 20000, 10**5
# times = [randint(3, 100) for _ in range(m)]
#
# users = [User(i) for i in times]
# start = t()
# while n > 0:
#     users.sort()
#     current_user = users[0]
#     n -= 1
#     current_time = current_user.current_time
#     current_user.next()
#
# print(current_time, t() - start)
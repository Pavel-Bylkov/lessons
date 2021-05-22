from itertools import combinations_with_replacement

n, m, k = (int(i) for i in input().split())
costs = [int(input()) for _ in range(n)]
max_group = m
combs = {}
for i in range(n):
    for j in range(i, m):
        combs[i].append([x for x in range(i, j)])

result = []

i = 0

print(combs)
for current in combs:
    result[i] = 0
    for group in current:
        min_cost = min(group)
        max_cost = max(group)
        x = len(current)
        if x > 1:
            result[i] += (max_cost - min_cost) * x ** 2 + k
        else:
            result[i] += max_cost + k

print(result)

from itertools import product
Na, Nb, Nc = (int(x) for x in input().split())

versions = [
    [x for x in range(1, Na + 1)],
    [x for x in range(1, Nb + 1)],
    [x for x in range(1, Nc + 1)]
]

Q = int(input())
# Xi, Ki, Yi, Mi где A — 1, B — 2, C — 3.
if Q:
    rules = [[int(x) for x in input().split()] for _ in range(Q)]
else:
    rules = None

result = 0
if rules:
    for element in product(*versions):
        for rule in rules:
            if element[rule[0] - 1] >= rule[1] and element[rule[2] - 1] < rule[3]:
                break
        else:
            result += 1
else:
    for element in product(*versions):
        result += 1

print(result)

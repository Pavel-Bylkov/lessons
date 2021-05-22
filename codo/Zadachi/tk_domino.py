import itertools

first = [int(i) for i in input().split()]
second = [int(i) for i in input().split()]
all_comb = [(i[0], i[1], j[0], j[1]) for i in list(itertools.permutations(first))
            for j in list(itertools.permutations(second))]
for comb in all_comb:
    if comb[1] == comb[2]:
        print(*comb)
        break
else:
    print(-1)

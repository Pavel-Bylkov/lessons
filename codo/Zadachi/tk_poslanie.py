n = int(input())
a = [int(i) for i in input().split()]

max_height = [[x for x in range(i + 1, n) if a[i] < a[x]] for i in range(n - 1)]
result = []
for k in range(n - 1):
    current = k
    count = 1
    while current < n - 1 and len(max_height[current]) != 0:
        current = max_height[current][0]
        count += 1
    result.append(count)
result.append(1)
print(*result)


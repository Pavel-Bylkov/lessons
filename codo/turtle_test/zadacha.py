n, m = (int(x) for x in input().split())
length = [int(i) for i in input().split()]
width = [int(i) for i in input().split()]

real_length = [length[-1]]
max_length = length[-1]
for i in range(n - 2, -1, -1):
    if length[i] - max_length > 0:
        real_length.append(length[i] - max_length)
        max_length = length[i]

for plita in real_length[:]:
    if plita in width:
        real_length.remove(plita)
        width.remove(plita)
width.sort(reverse=True)
for plita in real_length[::-1]:
    for plecho in width[:]:
        if plita >= plecho:
            real_length.remove(plita)
            width.remove(plecho)
            break

print(m - len(width))
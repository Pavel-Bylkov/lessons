n = input()
count = 0
i = 0
N = len(n)
while i < N:
    if n[i].isalpha():
        count += 1
        i += 1
    else:
        j = i + 1
        while j < N and n[j].isdigit():
            j += 1
        count += int(n[i:j]) - 1
        i = j
print(count)

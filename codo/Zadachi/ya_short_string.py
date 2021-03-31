n = "A4B3C2XYZD4E3F3A6B28"
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

# обратная задача
S = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
def short_string(string):
    if len(string) == 0:
        return ""
    result = string[0]
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
            continue
        if count > 1:
            result += str(count)
            count = 1
        result += string[i + 1]
    if count > 1:
        result += str(count)
    return result
print(short_string(S))
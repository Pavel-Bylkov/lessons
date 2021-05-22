def is_glasn(symbol):
    return symbol in 'aeiouy'

s = input()

for i in range(len(s) - 1):
    if is_glasn(s[i]) and is_glasn(s[i + 1]):
        print("NO")
        break
else:
    print("YES")

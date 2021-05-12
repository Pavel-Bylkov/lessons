num = input()
flag = True
if num[0:2] == '7-':
    for i in range(len(num)):
        if i in [1, 5, 9] and num[i] == "-":
            continue
        elif not num[i].isdigit():
            flag = False
    if len(num) != 14:
        flag = False
else:
    for i in range(len(num)):
        if i in [3, 7] and num[i] == "-":
            continue
        elif not num[i].isdigit():
            flag = False
    if len(num) != 12:
        flag = False
if flag:
    print("YES")
else:
    print("NO")
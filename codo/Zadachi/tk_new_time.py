a, b, c, t = (int(i) for i in input().split())

last_day = t % (a * b * c)
seconds = last_day % c
minutes = last_day // c % b
hours = last_day // c // b
print(hours, minutes, seconds)

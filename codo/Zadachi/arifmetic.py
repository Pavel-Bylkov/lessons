import os
b = int(input())

hours = b // 60
minuts = b % 60

print(b, "мин - это", hours, "часов", minuts, "минут")
print(f"{b} мин - это {hours} часов {minuts} минут")
print(str(b) + " мин - это " + str(hours) + " часов " + str(minuts) + " минут")
os.system('cls||clear')
print("{} мин - это {} часов {} минут".format(b, hours, minuts))
print("%d мин - это %d часов %d минут" % (b, hours, minuts))

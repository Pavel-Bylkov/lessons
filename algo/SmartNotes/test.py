from time import time

stopwatch = input('1 - старт, 0 - стоп:')
while stopwatch != '0':
    if stopwatch == '1':
        start = time()
    else:
        print('Действие не найдено!')
    stopwatch = input('0 - стоп:')
end = time()
total = int(end - start)
print('Общее время:', total, 'c')

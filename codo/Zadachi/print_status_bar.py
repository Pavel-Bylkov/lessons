import time
symbol = input('Введи символ: ')

for i in range(19):
    print('{:20s} - {}'.format(symbol * (i+1), i), end='')
    time.sleep(.3)
    print('\r', end='')

print()
from turtle import *
from time import time
from pprint import pprint

pprint(dir())

start = time()
color('red', 'yellow')
begin_fill()
pensize(5)
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
end = time()



print(end - start, "sek")

mainloop()

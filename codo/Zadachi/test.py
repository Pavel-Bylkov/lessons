from random import randint
from operator import itemgetter
from pprint import pprint
n = {i: randint(-200, 200) for i in range(100)}
q = sorted(n, key=itemgetter())
pprint(q)


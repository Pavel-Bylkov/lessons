from random import randint
import re
from pprint import pprint
n = {i: randint(-200, 200) for i in range(10)}
q = sorted(n, key=n.get)
for k in q:
    print(k, ":", n[k])
regex = re.compile('<code>.*?</code>')
soup = '<code>asdsaf</code>''<code>345sdfgsgd dfg</code>''<code>sdfgsdfg456fhdf /n dtwrggf sdg</code>'
a = re.findall('<code>.*?</code>', soup)
print(a)
a = regex.findall(soup)
print(a)

s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')

def teorema():
    a5 = {i: i ** 5 for i in range(1, 151)}
    e5 = {i ** 5 for i in range(1, 151)}
    for a in a5:
        for b in a5:
            for c in a5:
                for d in a5:
                    if a5[a] < a5[b] < a5[c] < a5[d] and a5[a] + a5[b] + a5[c] + a5[d] in e5:
                        return a, b, c, d, (a5[a] + a5[b] + a5[c] + a5[d]) ** (1/5)
    return None
print(teorema())

def summa_kubov():
    a3 = {i: i ** 3 for i in range(1, 50)}
    sum_a3 = {}
    res = []
    for a in a3:
        for b in a3:
            if a < b:
                sum3 = a3[a] + a3[b]
                if sum3 in sum_a3:
                    print(sum3, "=", sum_a3[sum3], "=", a, b)
                    res.append(sum3)
                else:
                    sum_a3[sum3] = (a, b)
    print(sorted(res)[0:5])

summa_kubov()
import sys
from collections import defaultdict
from datetime import datetime, timedelta

input = sys.stdin.readline

n, l, f = input().split()
n, f, rental = int(n), int(f), timedelta(days=int(l[:3]), hours=int(l[4:6]), minutes=int(l[7:]))
minute = timedelta(minutes=1)
table = defaultdict(dict)
product = defaultdict()
for _ in range(n):
    line = input()
    now = datetime.strptime(line[:16], '%Y-%m-%d %H:%M')
    part, name = line[16:].split()
    product[name] = product.get(name,0)
    if table[name].get(part):
        timediff = now - table[name][part]
        if timediff > rental:
            product[name] += ((timediff - rental) // minute) * f
        del table[name][part]
    else:
        table[name][part] = now

ret = [(k, v) for k, v in product.items() if v]
ret.sort()
if ret:
    for name, val in ret:
        print(name, val)
else:
    print(-1)
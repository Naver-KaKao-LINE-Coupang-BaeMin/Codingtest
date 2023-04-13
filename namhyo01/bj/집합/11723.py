import sys
input = sys.stdin.readline

m = int(input())
S = 0
for _ in range(m):
    op, *x = input().rstrip().split()
    if op == 'add':
        S |= 1 << int(x[0])
    elif op == 'remove':
        S &= ~(1 << int(x[0]))
    elif op == 'check':
        print(1 if S & (1<<int(x[0])) else 0)
    elif op == 'toggle':
        S ^= 1<<int(x[0])
        pass
    elif op == 'all':
        S |= (1<<21)-1
        pass
    else:
        S = 0
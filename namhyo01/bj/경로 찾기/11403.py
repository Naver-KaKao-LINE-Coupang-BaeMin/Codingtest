import sys
input = sys.stdin.readline
n = int(input())
inf = float('inf')
g = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k] == 1 and g[k][j] == 1:
                g[i][j] = 1
for i in g:
    for j in i:
        print(j,end=' ')
    print()
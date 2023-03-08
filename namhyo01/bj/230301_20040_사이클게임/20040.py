import sys
input = sys.stdin.readline

player1 = player2 = 0

n,m = map(int, input().split())
dots = [i for i in range(n+1)]

def find_parent(x):
    if x!=dots[x]:
        dots[x] = find_parent(dots[x])
    return dots[x]

def union(a,b,idx):
    a = find_parent(a)
    b = find_parent(b)
    if a==b:
        print(idx)
        exit(0)
    else:
        dots[max(a,b)] = min(a,b)

ans = 0
for i in range(1,m+1):
    a,b = map(int, input().split())
    union(a, b,i)
print(ans)
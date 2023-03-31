import sys
input = sys.stdin.readline
n,m,k = map(int, input().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x,y)] = min(x,y)

A = [0]+list(map(int, input().split()))

for _ in range(m):
    v,w = map(int,input().split())
    if v != w:
        union(v,w)
cnt = 0
check = [False for _ in range(n+1)]
temp = k
money = {}
for i in range(1,n+1):
    x = find(i)
    if x in money:
        money[x] = min(money[x], A[i])
    else:
        money[x] = A[i]
print('Oh no' if sum(money.values()) > k else sum(money.values()))
# for i in range(1,n+1):
#     if check[i]: continue
#     check[i] = True
#     min_money = float('inf')
#     cc = 0
#     for j in range(1,n+1):
#         if find(j) == i:
#             min_money = min(A[j], min_money)
#             cc += 1
#             check[j] = True
#     if temp>=min_money:
#         temp -= min_money
#         cnt += cc
#     else:
#         break
# if cnt != n:
#     print('Oh no')
# else:
#     print(k-temp)
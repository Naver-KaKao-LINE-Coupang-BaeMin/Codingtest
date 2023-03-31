import sys
input = sys.stdin.readline

n = int(input())
ids = list(map(int, input().split()))
max_id = max(ids)
parent = [i for i in range(max_id+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x,y)] = min(x,y)

sosu = list(range(max_id+1))
# 소인수분해용
def erasto(n):
    m = int(n**0.5)
    for i in range(2,m+1):
        if sosu[i] == i: # 소수이면
            for j in range(i*2,n,i): 
                # 최소 약수 저장
                if sosu[j] == j:
                    sosu[j] = i


# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b, a%b)
# k = 1
erasto(max_id+1)
for id in ids:
    if sosu[id]==id: continue
    temp = id
    while temp > 1:
        union(id, sosu[temp]) # id와 약수 한개
        temp //= sosu[temp] # 그리고 그다음 약수

cnt = {}
for id in ids:
    cnt[find(id)] = cnt.get(find(id),0) + 1
print(max(cnt.values()))




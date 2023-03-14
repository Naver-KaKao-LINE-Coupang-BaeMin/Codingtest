import sys
input = sys.stdin.readline

n,k = map(int, input().split())
a = list(map(int, input().split()))
alpha = {}
start = end = 0
ans = 0
while True:
    if start >= n or end >= n:
        break
    data = alpha.get(a[end],0)
    if data >= k:
        alpha[a[start]]-=1
        start += 1
        continue
    else:
        alpha[a[end]] = data + 1
        end+=1
        ans = max(ans, (end-start))
print(ans)
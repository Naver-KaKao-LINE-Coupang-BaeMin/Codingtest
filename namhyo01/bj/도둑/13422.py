import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    maps = list(map(int, input().split()))
    ans = 0
    if n==m:
        if sum(maps) < k:
            print(1)
            continue
        else:
            print(0)
            continue
        
    start, end = 0, m
    prefix_sum = sum(maps[0:m])
    while start < n:
        prefix_sum -= maps[start]
        prefix_sum += maps[end%n]
        if prefix_sum < k:
            ans += 1
        start += 1
        end += 1
    print(ans)

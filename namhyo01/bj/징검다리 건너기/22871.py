import sys
input = sys.stdin.readline
n = int(input())
rocks = list(map(int, input().split()))

K = [float('inf') for _ in range(n)]
K[0] = 0
def solve():
    for i in range(1,n):
        for j in range(0,i):
            K[i] = min(K[i], max(((i-j) * (1+abs(rocks[i]-rocks[j]))), K[j]))
    print(K[n-1])

def solve2():
    left, right = 0,(n-1) * (1+abs(rocks[n-1]-rocks[0]))
    while left<=right:
        mid = (left+right)//2
        visited = [False for _ in range(n)]
        visited[0] = True
        for i in range(n-1):
            if not visited[i]: continue
            for j in range(i+1,n): # 그 이후 체크
                p = (j-i) * (1+abs(rocks[j]-rocks[i]))
                if p <= mid:
                    visited[j] = True
        if visited[n-1]:
            right = mid-1
        else:
            left = mid+1
    print(right+1)
                

solve2()
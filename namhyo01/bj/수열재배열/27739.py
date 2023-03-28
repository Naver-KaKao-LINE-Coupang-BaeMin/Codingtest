import sys
from bisect import bisect_left
input = sys.stdin.readline
n,k = map(int, input().split())
a = list(map(int, input().split()))
a = [2001] + a + [0]
l = [0]+[1]*n+[0]
r = [0]+[1]*n+[0]
for i in range(2,n+1):
    if a[i] > a[i-1]:# 왼쪽보다 오른쪽이 증가한다면
        l[i] += l[i-1]
    if a[-i] > a[-i-1]: # 끝값이 그 전값보다 크다면
        r[-i-1] += r[-i]
ans = k
for i in range(1, len(a)-k):
    arr = a[i:i+k] # 리스트를 자르고
    high_l = low_r = 0 # 왼쪽보다 큰가, 오른쪽 보다 작은가
    for j in arr:
        if j < a[i+k]:
            low_r+=1
        if j > a[i-1]:
            high_l+=1
    ans = max(ans, high_l + l[i-1], low_r + r[i+k])
    if high_l == low_r == k:
        ans = max(ans, l[i-1] + k + r[i+k])


# def LIS(arr):
#     ans = 0
#     cnt = 1
#     for i in range(1,n):
#         if arr[i-1] < arr[i]:
#             cnt += 1
#             ans = max(ans, cnt)
#         else:
#             cnt = 1
#     ans = max(ans, cnt)
#     return ans


# def getList(arr):
#     arr.sort()
#     ans = []
#     for _ in range(k):
#         arr = arr[-1:-2:-1]+arr[0:-1]
#         ans.append(arr)
#     return ans
# ans = 0
# for i in range(n-k+1):
#     _a = getList(a[i:i+k])
#     for j in _a:
#         ans = max(ans,LIS(a[0:i] + j + a[i+k:]))
print(ans)
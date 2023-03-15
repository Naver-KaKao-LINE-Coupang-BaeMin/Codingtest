import sys
input = sys.stdin.readline
n,s = map(int, input().split())
nums = list(map(int, input().split()))
start = end = 0
ans = float('inf')
prefixSum = nums[start]
while True:
    if start >= n:
        break
    if prefixSum >= s:
        ans = min(ans, end - start + 1)
        prefixSum -= nums[start]
        start += 1
    else:
        if end == n-1:
            break
        end += 1
        prefixSum += nums[end]
print(0 if ans == float('inf') else ans)
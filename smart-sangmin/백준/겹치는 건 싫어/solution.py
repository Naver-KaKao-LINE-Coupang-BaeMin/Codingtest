import sys

input = sys.stdin.readline
N, K = map(int, input().split())

nums = list(map(int, input().split()))
answer = -1

cnt = {}
left, right = 0, 0

while right < N:
    if not cnt.get(nums[right], False):
        cnt[nums[right]] = 1
    else:
        if cnt[nums[right]] > K:
            cnt[nums[left]] -= 1
            left += 1
        else:
            cnt[nums[right]] += 1
            right += 1
    answer = max(answer, right - left)
print(answer)

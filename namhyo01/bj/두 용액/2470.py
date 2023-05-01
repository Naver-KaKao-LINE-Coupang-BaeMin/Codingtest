import sys
input = sys.stdin.readline


n = int(input())
features = list(map(int, input().split()))
features.sort()
left,right = 0, n-1
before = abs(features[left] + features[right])
ans_left, ans_right = features[left], features[right]
while left < right:
    sum = features[left] + features[right]
    if sum == 0:
        print(features[left], features[right])
        exit(0)
    if abs(sum) < before:
        ans_left, ans_right = features[left], features[right]
        before = abs(sum)
    if sum > 0: right -= 1
    else: left += 1
print(ans_left, ans_right)
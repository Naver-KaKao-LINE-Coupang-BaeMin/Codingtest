import sys
from bisect import bisect_left, bisect_right
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
students = list(map(int, input().split()))
start = 0
e = float('inf')
steak = 0

for mid in range(1, n):
    leftSum = students[mid-1]
    rightSum = students[mid]
    left = mid-1
    right = mid
    while True:
        diff = abs(leftSum - rightSum)
        if diff == e:
            steak = max(steak, leftSum+rightSum)
        elif diff < e:
            e = diff
            steak = leftSum+rightSum
        if leftSum < rightSum: # left가 더 작으니 증가 시킨다
            if left == 0:
                break
            left -= 1
            leftSum += students[left]
        elif leftSum > rightSum:
            if right == n-1:
                break
            right += 1
            rightSum += students[right]
        else:
            if left == 0 or right == n-1:
                break
            left -= 1
            right += 1
            leftSum += students[left]
            rightSum += students[right]


print(steak)

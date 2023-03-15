import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def divide_group(left, right):
    global answer
    for mid in range(1, N):
        left = mid - 1
        right = mid
        while True:
            if left < 0 or right >= N or left >= right:
                break
            left_group = sum[mid - 1] - (sum[left - 1] if left - 1 >= 0 else 0)
            right_group = sum[right] - sum[mid - 1]
            total = left_group + right_group
            diff = abs(left_group - right_group)

            if answer[0] > diff or (answer[0] == diff and answer[1] < total):
                answer = (diff, total)
            if left_group > right_group:
                right += 1
            elif left_group < right_group:
                left -= 1
            else:
                right += 1
                left -= 1


input = sys.stdin.readline
N = int(input())
steak = list(map(int, input().split()))
sum = []
check = [[False] * N for _ in range(N)]
answer = (sys.maxsize, -sys.maxsize)  # 차이, 무게합
temp = 0
for i in range(len(steak)):
    temp += steak[i]
    sum.append(temp)

divide_group(0, N - 1)
print(answer[1])

"""
5 3
2 1 5 3 4

7 3
3 2 1 7 4 5 6
"""


def check_left(start, end):
    cnt = 1  # 자기 자신 한 개
    for i in range(start, end):
        if nums[end] > nums[i]:
            cnt += 1
    for i in range(end + 1, N):
        if nums[end] > nums[i]:
            break
        cnt += 1
    return cnt


def check_right(start, end):
    cnt = 1  # 자기 자신 한 개
    for i in range(start, end):
        if nums[start - 1] < nums[i]:
            cnt += 1
    for i in range(start - 2, -1, -1):
        if nums[start - 1] < nums[i]:
            break
        cnt += 1
    return cnt


N, K = map(int, input().split())
nums = list(map(int, input().split()))
answer = -1
start, end = 0, K
while end <= N:
    if start == 0:
        left_cnt = check_left(start, end)
        answer = max(left_cnt, answer)
        print(left_cnt, -1)
    elif end == N:
        right_cnt = check_right(start, end)
        answer = max(right_cnt, answer)
        print(-1, right_cnt)
    else:
        left_cnt = check_left(start, end)
        right_cnt = check_right(start, end)
        if right_cnt + left_cnt - K == N:
            answer = N
            break
        answer = max(right_cnt, left_cnt, answer)
        print(left_cnt, right_cnt)
    start += 1
    end += 1
print(answer)

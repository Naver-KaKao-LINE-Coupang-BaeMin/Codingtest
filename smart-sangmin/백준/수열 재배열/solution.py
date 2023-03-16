"""
5 3
2 1 5 3 4

7 3
3 2 1 7 4 5 6
"""
N, K = map(int, input().split())
nums = [2001] + list(map(int, input().split())) + [0]
order_cnt = [0] + [1] * N + [0]
rev_order_cnt = [0] + [1] * N + [0]

for i in range(2, N + 1):
    if nums[i] > nums[i - 1]:
        order_cnt[i] += order_cnt[i - 1]
    if nums[-i] > nums[-i - 1]:
        rev_order_cnt[-i - 1] += rev_order_cnt[-i]

answer = K
for index in range(1, N - K + 2):
    greater = less = 0
    for i in range(K):
        greater += 1 if nums[index - 1] < nums[index + i] else 0
        less += 1 if nums[index + K] > nums[index + i] else 0
    answer = max(
        answer,
        greater + order_cnt[index - 1],
        less + rev_order_cnt[index + K],
        order_cnt[index - 1] + K + rev_order_cnt[index + K]
        if K == greater == less
        else -1,
    )
print(answer)

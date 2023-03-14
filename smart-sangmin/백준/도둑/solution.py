import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    village = list(map(int, input().split()))
    answer = 0
    left, right = 0, M - 1
    SUM = sum(village[left : right + 1])
    if N == M:
        if SUM < K:
            answer += 1
    else:
        while True:
            if SUM < K:
                answer += 1
            SUM -= village[left]
            left += 1
            right = (right + 1) % N
            SUM += village[right]
            if right == M - 1:
                break
    print(answer)

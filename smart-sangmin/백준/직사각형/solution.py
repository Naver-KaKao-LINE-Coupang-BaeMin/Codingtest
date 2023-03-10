"""
여러개 X
사용하지 않아도 됨
직사각형 하나 이상 만들어도 됨

막대를 길이를 1만큼 줄일 수 있음, 증복 X

직사각형 넓이 합의 최대

가장 긴 쌍을 찾고
그 다음 긴 쌍을 찾는다


4
5 5 6 6

4
4 5 2 3

4
2 4 6 8

6
5 6 6 3 4 4

9
10 3 4 4 4 5 6 6 6

10
10 10 10 10 10 10 10 10 10 10

4
100000 100000 100000 100000

10,000,000,000
"""

N = int(input())
sticks = list(map(int, input().split()))
sticks.sort()
edge1 = -1
edge2 = -1

answer = 0
i = N - 1
while i > 0:
    if sticks[i] == sticks[i - 1]:
        if edge1 == -1:
            edge1 = sticks[i]
        elif edge2 == -1:
            edge2 = sticks[i]
            answer += edge1 * edge2
            edge1, edge2 = -1, -1
        i -= 2

    elif sticks[i] - 1 == sticks[i - 1]:
        if edge1 == -1:
            edge1 = sticks[i] - 1
        elif edge2 == -1:
            edge2 = sticks[i] - 1
            answer += edge1 * edge2
            edge1, edge2 = -1, -1
        i -= 2

    else:
        i -= 1
print(answer)

import sys
from itertools import combinations
'''
최소 가격

조를 짤 때 최대한 키차이가 안나는 애들로 짜야됨

*정렬되어 있음
'''
N, K = map(int, input().split())
students = list(map(int, input().split()))
diff = []

for i in range(len(students) - 1):
    diff.append(students[i + 1] - students[i])
diff.sort()
print(sum(diff[:N-K]))
# answer = sys.maxsize
# for com in combinations(range(N-1), K-1):
#     temp = 0
#     prev = 0
#     for cur in com:
#         temp += students[cur] - students[prev]
#         prev = cur + 1
#     temp += students[N-1] - students[prev]
#     answer = min(answer, temp)
# print(answer)

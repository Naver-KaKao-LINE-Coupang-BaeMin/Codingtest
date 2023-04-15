import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
'''
    d일안에 와서 강연 => p준다
    가장 많이 벌게하자
    하루에 최대 한곳만 가능
    그런데
    1 -> 5
    2 -> 10
    2 -> 20
    이러면 30이 답이다 => 2일 안에 가능하므로
    일단 d일 기준 정렬은 필요는 하다
'''
day = 0
workable = []
ans = 0
for _ in range(n):
    p,d = map(int, input().split())
    workable.append([d,p])
workable.sort() # 날짜 기준 정렬
'''
5,1
10,2
20,2
이럴때 내가 과연 10, 20을 어떻게 골라낼수 있는가
기존
1 2
1 20 
2 8 
2 100 
3 10
10 50
20 5
여기서 우린
20 100 10 50 5 이렇게 골라야 한다

일단은 다 넣어보자 모든 경우를 => 지난 날은 어떻게 체크하는가? =>
당연히 최대한 많이 뽑아먹을려면 하루에 한번씩 일을 해야한다
== 날짜 == 일한 개수 => 그럼 일한 개수가 날짜이니 이걸 체크해서 제일 작은 값을 버린다? => 되나
'''
temp = []
for d, p in workable:
    heappush(temp, p)
    if d < len(temp): # len(temp) => 현재까지 몇일 일했는가
        heappop(temp) # => 만약 현재 일하는 것보다 더 많이 일했다면 그 만큼 빼자(하루기준으로 따지니 하나만 빼면 ok일듯)
# print(temp)
print(sum(temp))
# print(sum(day.values()))
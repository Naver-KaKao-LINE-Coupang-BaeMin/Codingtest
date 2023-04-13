import sys
input = sys.stdin.readline
MAX = 1001
'''
    위상 정렬 문제 -> 어떤 것을 해야만 다음 것을 할 수 있다.
    큐를 이용
'''
inDeg = [0 for _ in range(MAX)] # 진입 차수
graph = [[] for _ in range(MAX)]# 연결 리스트 생성
queue = []
n,m = map(int,input().split())

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    inDeg[b] += 1
# 큐 추가
for i in range(1,n+1):
    if not inDeg[i]:
        queue.append(i)
res = {}
temp = 1
# res = [float('inf') for _ in range(n+1)]
while True:
    nq = []
    for now in queue:
        # res.append(temp)
        # res[now] = temp
        # if res[now] == float('inf'):
        res[now] = temp
        for next in graph[now]:
            inDeg[next] -= 1
            if inDeg[next] == 0:
                # temp += 1
                # res[next] = min(res[next], res[now]+1)# 다음 번에 연결되는 애들은 지금거랑 현재까지 기록된 횟수랑 비교한다
                nq.append(next)
    if not nq:
        break
    queue = nq
    temp += 1
for i in range(1,n+1):
    print(res[i],end=' ')
# print(*res[1:],sep=' ')

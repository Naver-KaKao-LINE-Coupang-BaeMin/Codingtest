import sys
input = sys.stdin.readline

k,n,f = map(int, input().split())
friends = [[] for _ in range(n+1)]

checked = [0 for _ in range(n+1)]
def dfs(now, arr, check_num):
    if len(arr) == k: #조건 해당
        print(*arr ,sep ='\n')
        exit(0)
    for i in range(now+1, n+1):
        '''1 = >2 ...3..4 => 3..4..5
        돌면서 체크해보자일단
        '''
        if checked[i] == check_num: continue
        flag = True
        for j in arr:
            if j not in friends[i]: flag = False # 모두가 서로 친구여야하는 조건이었구나...
        if flag:
            checked[i] = check_num
            dfs(i, arr+[i], check_num)

for _ in range(f):
    a,b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(1,n+1):
    dfs(i,[i],i)

print(-1)
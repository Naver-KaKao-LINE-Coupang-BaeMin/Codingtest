import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    maps = list(map(int, input().split()))
    ans = 0
    if n==m:
        if sum(maps) < k:
            print(1)
            continue
        else:
            print(0)
            continue
        
    start, end = 0, m
    prefix_sum = sum(maps[0:m])
    while start < n:
        prefix_sum -= maps[start]
        prefix_sum += maps[end%n]
        if prefix_sum < k:
            ans += 1
        start += 1
        end += 1
    print(ans)
'''
도메인 관리자 문제\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
B형식 쿼리 문제
N명의 작업자와 쿼리 처리자가 있음. 쿼리 처리자는 URL을 받아서 각 작업자에게 배분해야 한다. 조건이 좀 많음.

한번 방문한 url은 다시 방문하지 않는다.

어떤 도메인을 가진 url을 처리중이라면 그것과 같은 도메인의 url은 처리하지 않는다.

처리 시작 시간을 S, 종료 시간을T라고 하면 그 도메인은 S+3T에 다시 방문할 수 있다.



INIT(int N, string url)
작업자는 N명으로 초기화, 1부터 N까지로 이름붙인다. 초기 url을 받는데, 이는 시간 0에 1번이 파싱했다고 가정한다. 실 문제에서는 C언어 스타일로 url이 주어졌다.

newURL(int tTime, int parserID, string url)
파싱중에 parserID 작업자가 tTime 시간에 새 url을 발견함

assign(int tTime)
tTime시간에 지금까지 미뤄둔 url중 하나를 뽑아 작업자에게 할당함.
가능한 것이 없거나 작업자가

'''

'''
N×N 미로 M명의 사람 K턴 1개의 출구
시뮬레이션 문제
시뮬레이션은 0턴-사람 이동 - 회전 -1턴 순으로 진행
K턴이 되면 시뮬레이션 종료
K턴 이전에 모든 사람이 탈출하면 회전 없이 종료

거리는 xy 절댓값 차로 구한다
각 사람은 매턴 1만큼 출구에 가까워지는 방향으로 이동한다
이동할 때 멀어지거나 이동이 불가능하면 이동x
Y축방향 우선으로 이동한다.

사람이 이동을 마친 후에는 미로가 회전한다. 출구와 적어도 한 사람을 포함하는 가장 작은 정사각형을 찾고 그 정사각형을 시계방향으로 90도 돌린다.
미로는 0:빈칸 1~9:벽의 내구도로 주어진다. 벽은 자신이 회전할 때마다 내구도가 1씩 줆.
시뮬레이션이 끝난 뒤 각 사람이 걸은 칸 수와 출구의 위치를 출력할 것.
'''

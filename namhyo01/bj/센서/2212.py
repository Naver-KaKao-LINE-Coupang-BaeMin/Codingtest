import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
if k>=n:
    print(0)
    exit(0)
'''
1 3 / 6 7 9 => 이래서 K=2
그럼 K-1개 만큼의 구분을 해주자
기준을 거리기준으로 잡자
'''
dis = [sensor[i+1] - sensor[i] for i in range(n-1)]
dis.sort(reverse=True) # 내림 차순 정렬 => 그러면 그 만큼 빼지게 되니
print(sum(dis[k-1:]))

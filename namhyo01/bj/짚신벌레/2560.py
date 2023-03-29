import sys
input = sys.stdin.readline
a,b,d,n = map(int,input().split())
if a>n:
    print(1)
    exit(0)
'''
day 태어난 날 기준
0 0
1 0
2 0 2
3 0 2 3
4 0 2 3 4 
5 0 2 3 4 5 5
6 2 3 4 5 5 6 6 
살 수 있는 애들은? => 총 애들 - 죽은 놈들
이게 맞나
그런데 태어나는 애들도 다르다
그럼 태어나는 애들은? 특정 날에 태어날수 있는 범위를 생각해보자
5일 기준 새끼는 3일째부터 가능하다
그 뜻은
day-now가 a이상이라는 의미
반대로 못낳는 케이스는 b일 째부터이니 day-now가 b-1까지다
a <= day-now <= b-1 =>이걸 만족해야하는 now는
day-a>=now >= -b+1+day
-b+1+day <= now <= day-a가 된다 => 이걸 dp로 계산을 해보면
dp[day] = 현재까지 살아있는 애들 + 새로 태어난애들 중 추가[day-a] - 죽는애들[day-b]
'''
bugs = [0 for _ in range(n+1)] # 낳을 수 있는 아이들
bugs[0] = 1 # 첫날 넣기 
able = 0
ret = 1
for i in range(1,n+1):
    if i>=a: #a이상이면 그만큼을 더해주자
        able += bugs[i-a]
        able %= 1000
    if i>=b: # 이젠 못낳는 애들 추가하자
        able -= bugs[i-b]
        able %= 1000
    bugs[i] = able #bug수 갱신
    print(able)
    ret += able
    '''
        죽는애들도 비슷할듯
        day-now >= d이거면 죽은거다
        now <= -d+day
    '''
    if i>=d:
        ret -= bugs[i-d]
print(ret%1000)







    



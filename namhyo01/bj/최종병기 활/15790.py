import sys
input = sys.stdin.readline
n,m,k = map(int, input().split())
x = []
for _ in range(m):
    x.append(int(input()))
'''
    k개 만큼 고무줄을 잘라야 한다 => 중요
    이 k개중 가장 작은 고무줄 길이로 활 길이 결정
    가장 긴 활은? => 몰?루
'''
ans = n
def calcLength(a,b):
    return (b-a)%n
if k==1:
    print(ans)
    exit(0)
if m==k:
    for i in range(m-1):
        ans = min(calcLength(x[i],x[i+1]),ans)
    print(ans)
    exit(0)
'''
    이분탐색으로 어떻게 풀지 생각하자
    찾고싶은값? 길이지 => 활을 길이를 최대한 길게
    mid를 활의 길이라 생각하자

'''
l,r = 0,n # 초기 최소값, 최대값

def solve(start,mid):
    idx = (start+1)%m # => 그 다음 index
    cnt = 0
    cur = start
    while idx != start: # index가 i까지 오면 원형 다 돈 것이다.   
        '''
            여기서 하나씩 만들어가보자
            mid가 활의 길이라 가정했으니
            찾을 값은 적어도 이거 이상이여야 한다
        '''
        if calcLength(x[cur],x[idx]) >= mid:
            cnt += 1
            cur = idx
            if cnt == k-1:
                # 마지막 제외 다 만든 상태
                # 마지막 길이는 현재까지~처음위치 => mid보다 이상이면 True
                if calcLength(x[cur], x[start]) >= mid: return True
                break
        idx = (idx+1)%m # 갱신
    return False

while l <= r: # l = mid+1, r = mid
    mid = (l+r)//2 # 지금 활의 길이
    flag = False
    for i in range(m): # m만큼 돌면서 홈의 빈 곳을 찾자 => 시작 위치 선정
        if solve(i,mid):
            # 참이라면 mid값으로 통과가 가능하다
            flag = True
            break
    if flag: l = mid+1
    else: 
        r = mid-1

print(r)





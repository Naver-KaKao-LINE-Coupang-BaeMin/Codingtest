import sys
input = sys.stdin.readline

n,d,k,c = map(int, input().split())
chobab = []
for _ in range(n):
    chobab.append(int(input()))
# chobab += chobab
left = right = 0
cnt = 0
choose = {}
choose[c] = 1 # 쿠폰선택은 일단 1로 체크(골랐다 가정하자)
while right < n+k: # 오른쪽으로 증가하면서 보자
    '''
        하나씩 처음과 끝을 두고 계산하자 길이고 k가 되는 순간 이제 left도 움직이자
    '''
    choose[chobab[right%n]] = choose.get(chobab[right%n], 0) + 1 # 현재 기준에서 count증가
    if right >= k-1: # right가 k-1까지 왔다는 것은 0~k-1 => k개 연속 고른거다
        cnt = max(cnt, len(choose))
        # 그리고 다음 right를 움직이기 위해서눈 left가 감소
        choose[chobab[left%n]] -= 1
        if choose[chobab[left%n]] == 0:
            del choose[chobab[left%n]]
        left += 1
    right +=1
print(cnt)
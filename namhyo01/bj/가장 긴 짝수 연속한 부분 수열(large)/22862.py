import sys
input = sys.stdin.readline
n,k = map(int, input().split())
S = list(map(int, input().split()))

left = right = 0
'''
    짝수 연속
    둘다 하나씩 움직이면서 계산
    두 사이 안의 홀수가 k개라면 다음으로 right만 이동
    넘어가면 left가 홀수가 나올떄까지 이동
'''
cnt = length = 0

while right < n:
    if cnt > k: # 홀수의 개수가 k개보다 커진다면
        # 그럼 left에서 계속해서 증가한다 
        if S[left] % 2 == 1:# 홀수이면
            cnt -= 1
        left += 1
        continue
    else: # cnt가 k랑 같거나 작다면
        if S[right] % 2 == 1:
            cnt += 1
        right += 1
    length = max(length, right-left-cnt)
print(length)



import sys
input = sys.stdin.readline
n = int(input())
sticks = list(map(int, input().split()))
sticks.sort(reverse=True)
tot_sticks = n//4 # 이정도는 만들어야 한다!
ans = 0
sero = 0
garo = 0
idx = 0
checked = [False for _ in range(n+1)]

for i in range(n-1):
    if checked[i]:
        continue
    if sticks[i] == sticks[i+1]:
        checked[i] = checked[i+1] = True
        if sero == 0:
            sero = sticks[i]
        else:
            ans += sero * sticks[i]
            sero = 0
    if sticks[i] == sticks[i+1]+1:
        checked[i] = checked[i+1] = True
        if sero == 0:
            sero = sticks[i]-1
        else:
            ans += sero * (sticks[i]-1)
            sero = 0
print(ans)
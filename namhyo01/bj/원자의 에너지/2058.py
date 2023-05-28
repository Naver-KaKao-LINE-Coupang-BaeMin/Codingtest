import sys
input = sys.stdin.readline

'''
    원자가 높은 에너지 -> 낮은 에너지 => 에너지 차만큼 양성자 방출
    역은 필요하다

    a -> b의 길은 유일하다
    즉 같은 원자를 넣으면 안되고, 트리에서 서로 인접한 원자가 있으면 안된다.
    

'''

n,m = map(int, input().split())
atomic_energy = []
plus_energy = []
for _ in range(n):
    atomic_energy.append(int(input()))
for _ in range(m):
    plus_energy.append(int(input()))
'''
    이 문제는 + - 면서 다른애한테 도달할수 있는가?
    그러나 인접한 애가 존재하면 안된다.
'''
visited = {atom: False for atom in atomic_energy}
dp = {atom: [0,0] for atom in atomic_energy}

# 현재 아톰 기준
def dfs(atom):
    visited[atom] = True
    dp[atom][1] = atom # 넣는다고 한다면 현재 에너지이다.

    for p in plus_energy:
        if (atom + p) in visited and not visited[atom+p]:
            dfs(atom+p) # 다음걸로 가자
            dp[atom][0] += max(dp[atom+p][1],dp[atom+p][0]) # => 만약 안넣는다면 넣을때랑 안넣었을대중 큰값으로
            dp[atom][1] += dp[atom+p][0] # 무조건 안넣어야 한다 다음꺼는
        if (atom - p) in visited and not visited[atom-p]:
            dfs(atom-p) # 다음걸로 가자
            dp[atom][0] += max(dp[atom-p][1],dp[atom-p][0]) # => 만약 안넣는다면 넣을때랑 안넣었을대중 큰값으로
            dp[atom][1] += dp[atom-p][0] # 무조건 안넣어야 한다 다음꺼는
dfs(atomic_energy[0])
print(max(dp[atomic_energy[0]][0],dp[atomic_energy[0]][1]))





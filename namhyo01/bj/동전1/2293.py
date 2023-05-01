import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [0 for _ in range(k+1)]
for i in range(1,k+1):
    
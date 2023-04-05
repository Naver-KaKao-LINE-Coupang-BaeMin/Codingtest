import sys
input = sys.stdin.readline

n = int(input())
food = []
for _ in range(n):
    K, *food = input().split()
    print(food)
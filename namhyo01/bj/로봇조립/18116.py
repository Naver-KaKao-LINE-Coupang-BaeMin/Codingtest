import sys
input = sys.stdin.readline

n = int(input())
robot = [i for i in range(10**6+1)]
boopooms = [1 for _ in range(10**6+1)]
def find(x):
    if robot[x] != x:
        robot[x] = find(robot[x])
    return robot[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        robot[max(x,y)] = min(x,y)
        boopooms[min(x,y)] = boopooms[x]+boopooms[y]
for _ in range(n):
    ops = input().split()
    if len(ops) == 3:
        a, b = int(ops[1]), int(ops[2])
        union(a,b)
    else:
        a = int(ops[1])
        print(boopooms[find(a)])

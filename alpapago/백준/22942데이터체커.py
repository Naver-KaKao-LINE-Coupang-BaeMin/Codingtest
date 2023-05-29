import sys
input = sys.stdin.readline

n = int(input())

left = []
right = []
stack = []

for _ in range(n): 
    x,r= map(int,input().split())
    left.append(x-r)
    right.append(x+r)

left = [(i,idx) for idx,i in enumerate(left)]
right = [(i,idx) for idx,i in enumerate(right)]

left.extend(right)
left.sort(key = lambda x:x[0])

stack.append(left[0])

for i in range(1,len(left)):
    if len(stack) == 0:
        stack.append(left[i])
    elif stack[-1][1] == left[i][1]:
        stack.pop()
    else:
        stack.append(left[i])

if stack:
    answer = 'NO'
else:
    answer = 'YES'

print(answer)

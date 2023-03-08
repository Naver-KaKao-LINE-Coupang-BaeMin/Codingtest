import sys
input = sys.stdin.readline
ans = 0
temp = 1
ran = input().strip()
stack = []
inside = []
"""
(())
"""
for j in range(len(ran)):
    i = ran[j]
    if i=='(' :
        temp *= 2
        stack.append(i)
    elif i=='[':
        temp *= 3
        stack.append(i)
    elif i==')':
        if not stack:
            ans = 0
            break
        last = stack.pop()
        if last == '[':
            ans = 0
            break
        if ran[j-1]=='(':
            ans += temp
        temp = temp//2
    else:
        if not stack:
            ans = 0
            break
        last = stack.pop()
        if last == '(':
            ans = 0
            break
        if ran[j-1]=='[':
            ans += temp
        temp = temp//3
""""
[[[]]
"""
if len(stack)!=0:
    print(0)
else:
    print(ans)
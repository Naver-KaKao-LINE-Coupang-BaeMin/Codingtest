import sys
input = sys.stdin.readline

mid_reg = input().strip()
stack = []
res = ''
'''
 1. 괄호
 2. * /
 3. + - 순
'''
for s in mid_reg:
    if s.isalpha():
        res += s # 알파벳이라면 일단 추가
    elif s == '(': # 괄호는 결과에는 넣지는 않는다
        stack.append(s) # 값은 추가
    elif s == ')':
        # 괄호가 열리고 그 스택 안의 것들은 싹다 추가
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop() # (제거
    elif s == '*' or s == '/':
        while stack and stack[-1] != '(' and (stack[-1] == '*' or stack[-1] == '/'):
            res += stack.pop()
        stack.append(s)
    elif s == '+' or s == '-':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(s)
while stack:
    res += stack.pop()
print(res)

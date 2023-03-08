brackets = input()
stack = []
temp = 1
answer = 0


for i in range(len(brackets)):
    if brackets[i] == "(":
        stack.append(brackets[i])
        temp *= 2
    elif brackets[i] == "[":
        stack.append(brackets[i])
        temp *= 3
    elif brackets[i] == ")":
        if not stack or stack[-1] != "(":
            answer = 0
            break
        if brackets[i-1] == "(":
            answer += temp
        temp //= 2
        stack.pop()
    elif brackets[i] == "]":
        if not stack or stack[-1] != "[":
            answer = 0
            break
        if brackets[i-1] == "[":
            answer += temp
        temp //= 3
        stack.pop()
    else:
        answer = 0
        break
if stack:
    print(0)
else:
    print(answer)

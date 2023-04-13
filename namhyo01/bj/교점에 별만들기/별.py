from collections import defaultdict
def solve(l_a,l_b):
    a,b,e = l_a
    c,d,f = l_b
    # 평행은 pass 그런데 겹치면? => 겹쳐도 out
    if a*d - b*c == 0:
        return False
    x = (b*f-e*d) / (a*d-b*c)
    y = (e*c-a*f) / (a*d-b*c)
    if x == int(x) and y == int(y):
        return int(x),int(y)
    return False

def solution(line):
    answer = []
    coords = defaultdict(set)
    max_x, min_x, max_y, min_y = -float('inf'),float('inf'),-float('inf'),float('inf')
    for i in line:
        for j in line:
            temp = solve(i,j)
            if temp:
                coords[temp[1]].add(temp[0])
                max_x = max(temp[0], max_x)
                max_y = max(temp[1], max_y)
                min_x = min(temp[0], min_x)
                min_y = min(temp[1], min_y)
        
    for i in range(max_y,min_y-1,-1):
        row = ''
        for j in range(min_x, max_x+1):
            if j in coords[i]:
                row += '*'
            else:
                row += '.'
        answer.append(row)

    return answer
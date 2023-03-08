import sys
from itertools import permutations
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
m = list(map(int, input().split()))
'''
    중등부 2번 질수없다
    13321132 => 111 22 333 or 22 111 333 333 111 22
    
'''
cnt_nums = {}
locate = {}
locate_x = {}
checked = list(permutations([1,2,3],3)) # 경우의 수 => 모든 경우의 수
x = 0
for i in m:
    cnt_nums[i] = cnt_nums.get(i,0) + 1
    x+=1
'''
    각 원소별 개수를 센다(일단은)
    그리고 현재 checked에 만들 수 있는 모든 모양은 만들어져 있다...
    그럼 각 돌면서 그것들을 만들어가면서 최소개수를 구하자
    3*2*1 => 6번이니 크게 영향 안주겠지?

'''
ans = float('inf')
for i in checked:
    '''
        여기서 순서대로 맞추어야 한다.
        a,b,c 로 순서대로 값을 주었고...
    '''
    a,b,c = i[0],i[1],i[2]
    '''
        이젠 저 모양에서 돌아줘야겠다
    '''
    nm = deepcopy(m)    
    '''
        n만큼 돌면서 각각 비교 O(n)?
        n^2은 안될것같은데
        6n정도면 가능할지도...?
    '''
    
    change = [[0 for _ in range(4)] for _ in range(4)]
    for j in range(n):
        '''
            아 저 a,b,c의 순서에 맞춰서 작업하면 될거같다
        '''
        if j < cnt_nums[a]: #여기에 걸린다는 것은 아직 a부터 맞추어 지지 않았냐를 체크체크체크
            '''
                만약 아직 첫번째 껄로 정렬을 못했다면?
                일단 뒤에있는 a들을 싹 다 앞으로 바꿔주어야 겠지...
            '''
            if nm[j] != a: # 만약에 현재위치의 nm이 a가 아니라면
                '''
                    만약에 a가 거기에 있는게 아니라면 
                    count증가를 하면될려나
                    바꾼다는 의미를 생각해서 넣어보자
                '''
                change[a][nm[j]] +=1
        elif j < cnt_nums[a] + cnt_nums[b]: # 중앙 맞추기
            if nm[j] != b:
                change[b][nm[j]] += 1 # a랑 nm[j]가 서로 바꾼다는 의미이다
                
        else: # 마지막 맞추기
            if nm[j] != c:
                change[c][nm[j]] += 1 # a랑 nm[j]가 서로 바꾼다는 의미이다
    '''
        여기까지 오면 a,b,c가 각각 nm[j]랑 몇번이나 바뀌었는지 체크 가능
        그럼 경우의 수를 따져보자
        1 3 3 2 1 1 3 2
        123을 만들려면
        1은 2랑 바꿀필요가 없지...
        1은 3이랑만 바꾼다
        [1][3] = 2
        2는 1이랑 바꾼다
        [2][1] = 1
        3은 1과 2랑 바꾼다
        [3][1] = 1
        [3][2] = 1
        ------------
        321만들려면
        [3][1] = 1
        [2][1] = 1
        [1][2] = 1
        [1][3] = 1
    '''
    cnt = 0
    cnt = max(change[1][2], change[2][1])
    cnt += min(change[1][3], change[3][1])
    cnt += max(change[2][3], change[3][2])
    ans = min(cnt, ans)    
print(ans) # 뭐야 왜 4야



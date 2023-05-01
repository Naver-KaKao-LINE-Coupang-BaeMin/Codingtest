import sys
input = sys.stdin.readline


while True:
    n, k = map(int, input().split())
    if n==0 and k==0: break
    nodes = [-1] + list(map(int, input().split()))
    root = nodes[0]
    parent = [0 for i in range(n+1)]
    parent[0] = -1 # root의 부모가 있는가
    d = -1
    '''
        정리하자
        k의 부모의 형제들의 자식 노드 개수 => 사촌의 개수
        일단 부모들을 입력부터 하자
    '''
    temp = k
    for i in range(1,n+1): # 0은 그녀석꺼
        if nodes[i] != nodes[i-1]+1: # 왼쪽 부터 체크
            d+=1 
        parent[i] = d
        if nodes[i] == k:
            temp = i # k 위치 저장
    '''
        부모 depth저장 완료
        k도 저장 되어 있으니 
        [-1, 2, 2, 2, 3, 3, 4, 5, 5, 9, 10]
        여기서 15의 위치의 값은 4이다
        그럼 3의 부모는 => 1 그럼 다 돌면서 어떤 것의 부모도 1이면 정답이지 않으띾
        형제는 아니어야하니 부모는 달라야함
    ''' 
    k = temp
    cnt = 0
    for i in range(1,n+1):
        if parent[i] != parent[k] and parent[parent[k]] == parent[parent[i]]:
            cnt+=1

    print(cnt)
        
    
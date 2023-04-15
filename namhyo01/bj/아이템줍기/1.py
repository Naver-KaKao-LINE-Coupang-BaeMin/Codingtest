
'''
    이게 왜 bfs지 => 아이템을 줍는 최단 거리이니 
    근데 그 maps를 어떻게 표현해야할까...
    일단 겉 테두리를 표현해야겠다 => 어떻게? => 진짜 어떻게해야하지...?
        => 이걸 구현해야 하는데...
'''
'''
패스해버리네 어이가 없네... 
[[1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [3, 6], [2, 6], [2, 7], [2, 8], [3, 8], [4, 8], [4, 9], [5, 9], [6, 9], [6, 8], [7, 8]]

아니 아
이게 붙어있으니
3,5 => 3,6로 이동해버린다.......?
원래는 4,5로 가야한다 왜 이럴까
maps를 1로만 두고 방향을 안두니 이런것 같다
근데 방향을 저장할 방법은 없다
거리를 벌려보자 => 어떻게?
이 때가 2배를 활용할 때인듯하다 => 아마도?= > 될지는 모르겠다 2차시도

'''
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
checked  = [[False for _ in range(51*2)] for _ in range(51*2)]
maps = [[-1 for _ in range(51*2)] for _ in range(51*2)]
            
def calcMap(rectangle):
    for x1,y1,x2,y2 in rectangle:
        
        ''' 하지만... 겹쳐서 중단을 어떻게 해야하는가?
            너무 싫다
            머리 아프다
            공간도형 진짜 싫다...
        '''
        x1*=2
        x2*=2
        y1*=2
        y2*=2
        for i in range(x1, x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    maps[j][i] = 0 # 내부
                else:
                    if maps[j][i] != 0:
                        maps[j][i] = 1
                
        
def check(characterX, characterY, itemX, itemY):
    if characterX == itemX and characterY == itemY:
        return True
    return False
    
            
def bfs(characterX, characterY, itemX, itemY):
    queue = deque([])
    checked[characterX][characterY] = True
    queue.append([characterX, characterY,0,[[characterX,characterY]]])
    while queue:
        x,y,cnt,path = queue.popleft()
        if check(x,y,itemX,itemY):
            return cnt
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 1*2<=nx<=50*2 and 1*2<=ny<=50*2 and maps[ny][nx]==1 and not checked[nx][ny]:
                checked[nx][ny] = True
                queue.append([nx,ny,cnt+1,path+[[nx,ny]]])
                	# 미친... 3,4 => 3,5로 패스해버리네 어이가 없네... [[1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [3, 6], [2, 6], [2, 7], [2, 8], [3, 8], [4, 8], [4, 9], [5, 9], [6, 9], [6, 8], [7, 8]]
    return 0     
        
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    calcMap(rectangle)
    cnt = 0
    answer = bfs(characterX*2, characterY*2, itemX*2, itemY*2)
    return answer//2
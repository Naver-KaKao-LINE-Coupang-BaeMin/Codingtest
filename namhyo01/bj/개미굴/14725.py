import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data = None):
        self.children = {}
        self.data = data
        self.key = key
class Trie:
    def __init__(self):
        self.head = Node(None)
    def insert(self, strings):
        cur = self.head
        for string in strings:
            if string not in cur.children:
                cur.children[string] = Node(string)
            cur = cur.children[string]
        cur.data = string
    
    def dfs(self, depth, cur):
        # if cur.data: return # 끝이라는 이야기니
        children = dict(sorted(cur.children.items())) # 딕셔너리 정렬
        for k,v in children.items():
            print('--'*depth,k,sep='')
            self.dfs(depth+1, v)

# class Trie:
#     def __init__(self):
#         self.head = {}
    
#     def insert(self, string):
#         curNode = self.head
#         for s in string:
#             if s not in curNode: #포함되어 있지 않으면 추가
#                 curNode[s] = {} # 새롭게 추가
#             curNode = curNode[s] # curNode 갱신
#         curNode[-1] = True # 문자열의 끝을 알림
#     '''
#         현재 탐색 중인 깊이 (--를 위한)
#         현재 어디 노드를 가리키는지
#     '''
#     def dfs(self, depth, cur):
#         if -1 in cur: # 문자열의 끝을 알리는 순간
#             return
#         ''' 그게 아니라면 딕셔너리 안의 여러개들의 데이터를 정렬해주어야 한다 '''
#         cur = dict(sorted(cur.items())) # 딕셔너리 정렬
#         for k,v in cur.items():
#             print('--'*depth,k,sep='')
#             self.dfs(depth+1, v)

n = int(input())
food = []
trie = Trie()
for _ in range(n):
    K, *food = input().split()
    trie.insert(food)
trie.dfs(0,trie.head)
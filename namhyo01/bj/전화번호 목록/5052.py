import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key # 해당 노드의 문자가 들어간다
        self.data = data # 문자열이 끝나는 flag => 여기선 되돌아 갈 일 없게 마지막 문자에 문자열 저장
        self.children = {} # 자식 노드

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        current_node = self.head # 시작은 헤드로 (헤드는 빈값)
        for char in string: # 단어 하나하나 보자
            if char not in current_node.children: # 자식에 포함되어 있지 안핟면
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        if current_node.data:
            return True
        return False
    
    def starts_with(self, prefix):
        current_node = self.head
        words = []
        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return []
        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data: # 끝난 다면
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if next_node:
                current_node = next_node
                next_node = []
            else:
                break
        
        return words
    

t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    flag = False
    words = []
    for _ in range(n):
        s = input().rstrip()
        words.append(s)
        trie.insert(s)
    for i in words:
        if len(trie.starts_with(i))!=1:
            flag = True

    if flag: print('NO')
    else: print('YES')
import sys
input = sys.stdin.readline
t = int(input())

# def isPalin(string):
#     ll = len(string)
#     if ll%2==0:
#         temp = string[ll//2:]
#         return string[:ll//2]==temp[::-1]
#     else:
#         temp = string[ll//2+1:]
#         return string[:ll//2]==temp[::-1]

# def isSimilarPalin(string):
#     for i in range(len(string)):
#         new_str = string[:i] + string[i+1:]
#         if isPalin(new_str):
#             return True
#     return False
# # def isSimilarPalin(string):
# #     for i in range(len(string)):
# #         new_str = string[:i] + string[i+1:]
# #         if isPalin(new_str):
# #             return True
# #     return False

# def solve(string):
#     if isPalin(string):
#         return 0
#     elif isSimilarPalin(string):
#         return 1
#     return 2

def solve(string, l, r, drop):
    while l<r:
        if string[l] == string[r]: # 같으면
            l+=1
            r-=1
        else: # 다르면
            if not drop: # 아직 버리지 않았다면
                ans = solve(string, l+1, r, True) or solve(string,l,r-1,True)
                if ans:
                    print(1)
                else:
                    print(2)
                return False
            else: # 버렸다면
                return False
    if not drop:
        print(0)
    return True


for _ in range(t):
    temp = input().strip()
    # print(solve(temp))
    solve(temp,0,len(temp)-1,False)
    
    # print(temp[:(len(temp)//2)])
    # print(temp[len(temp)//2:])
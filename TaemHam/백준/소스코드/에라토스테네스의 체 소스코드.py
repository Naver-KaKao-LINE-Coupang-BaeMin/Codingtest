# n 이하의 모든 소수 구하기
n = 541 #int(input().strip())
n += 1
grp = [1] * (n//2)
for i in range(3, int(n**0.5)+1, 2):
    if grp[i//2]:
        grp[i*i//2::i] = [0] * len(grp[i*i//2::i])
    
arr = [2] + [2*i+1 for i in range(1, n//2) if grp[i]]
print(arr[-1])
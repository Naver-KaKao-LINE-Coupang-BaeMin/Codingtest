import sys
input = sys.stdin.readline

n,l,r,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = 0
def solve(start,tot,arr):
    global ans
    if l<=tot<=r and arr[-1]-arr[0] >= x:
        ans+=1
    for i in range(start+1,n):
        solve(i,tot+a[i],arr+[a[i]])
for i in range(n):
    solve(i,a[i],[a[i]])
print(ans)
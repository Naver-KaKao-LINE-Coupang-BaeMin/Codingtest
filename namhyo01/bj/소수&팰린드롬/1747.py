import sys
input = sys.stdin.readline



n = int(input())
prime = [True]*(10000000)
def erasto():
    for i in range(2,int(1000001**0.5)+1) :
        if prime[i]:
            for j in range(i+i,1000001,i):
                prime[j] = False
def ispalindrome(num):
    if num == num[::-1]:
        return True
    return False

erasto()
while True:
    if ispalindrome(str(n)) and prime[n]:
        print(n)
        break
    n+=1

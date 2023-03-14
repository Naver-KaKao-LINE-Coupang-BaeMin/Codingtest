def check_prime_number(n):
    if n == 1:
        return False
    for num in range(2, n//2+1):
        if n % num == 0:
            return False
    return True


N = int(input())

while True:
    if str(N) == str(N)[::-1]:
        if check_prime_number(N):
            print(N)
            break
    N += 1

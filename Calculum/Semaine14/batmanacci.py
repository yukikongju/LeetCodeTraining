# https://open.kattis.com/problems/batmanacci
# Solution: 
# (1) remark that sequence length is equal to fibonacci sequence
# (2) we can generate the length of the nth sequence with fibonacci. 
# (3) we know that the nth sequence is made of [seq n-2][seq n-1]. to 
# determine where to check, we check whether k < len(seq n-2)
# execute: python3 batmanacci.py < batmanacci/input1.in


def get_inputs():
    n, k = map(int, input().split())
    return n, k
    

def batmanacci_naive(n, k): # linear
    dp = ['' for _ in range(n)]
    dp[0], dp[1] = "N", "A"

    for i in range(2, n):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[-1][k-1]

def batmanacci(n, k):
    # 1. calculate length of nth sequence
    fib = fibonacci(n)

    # 2. 
    while n > 2:
        if k <= fib[n-2]:
            n -= 2
        else:
            k -= fib[n-2]
            n -= 1

    # 3. 
    if n == 1:
        return "N"
    elif n == 2: 
        return "A"
    else: 
        return "error"


def fibonacci(n):
    fib = [0]*(n+1)
    fib[0], fib[1] = 0, 1
    for i in range(2, n+1):
        fib[i] = fib[i-2] + fib[i-1]
    return fib

#  --------------------------------------------------------------------------

def test():
    print(batmanacci(7, 7))
    print(batmanacci(777, 777))
    

def main():
    n, k = get_inputs()
    answ = batmanacci(n, k)
    print(answ)
    

if __name__ == "__main__":
    main()

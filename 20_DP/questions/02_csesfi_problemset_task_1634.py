mod = 1000000007

dp = [-1] * 1000005

def f(n):
    if n == 0:
        return 1
    if dp[n] != -1:
        return dp[n]
    
    sum_val = 0
    for i in range(1, 7):
        if (n - i) < 0:
            break
        sum_val = (sum_val % mod + f(n - i) % mod) % mod
    
    dp[n] = sum_val % mod
    return dp[n]

def main():
    n = int(input())
    print(f(n))

if __name__ == "__main__":
    main()

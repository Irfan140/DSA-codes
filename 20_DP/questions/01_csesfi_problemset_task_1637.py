def get_digits(n):
    result = []
    while n > 0:
        if n % 10 != 0:
            # n%10 is the last digit
            result.append(n % 10)
        n = n // 10
    return result

dp = []

def f(n):
    if n == 0:
        return 0
    if n <= 9:
        return 1
    if dp[n] != -1:
        return dp[n]
    d = get_digits(n)
    
    result = float('inf')
    for i in range(len(d)):
        result = min(result, f(n - d[i]))
    dp[n] = 1 + result
    return dp[n]

# bottom up solution
def fbu(num):
    dp[0] = 0
    for i in range(10):
        dp[i] = 1  # base cases
    for n in range(10, num + 1):
        # n denotes state here
        # calculate dp[n]
        d = get_digits(n)
        result = float('inf')
        for i in range(len(d)):
            result = min(result, dp[n - d[i]])
        dp[n] = 1 + result
    return dp[num]

def main():
    global dp
    n = int(input())
    dp = [-1] * 1000005  # constraint given 10^5
    # print(f(n))
    print(fbu(n))

if __name__ == "__main__":
    main()

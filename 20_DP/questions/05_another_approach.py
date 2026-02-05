def main():
    n = int(input())
    f = [0] * (n + 10)
    m = int(input())
    
    for _ in range(m):
        L, R = map(int, input().split())
        f[L] += 1
        f[R + 1] -= 1
    
    # prefix sum
    for i in range(1, len(f)):
        f[i] = f[i] + f[i - 1]
    
    c = [0] * 10000005
    for i in range(n + 1):
        coins = f[i]
        c[coins] += 1
    
    for i in range(len(c) - 2, -1, -1):
        c[i] = c[i] + c[i + 1]
    
    q = int(input())
    for _ in range(q):
        num = int(input())
        print(c[num])

if __name__ == "__main__":
    main()

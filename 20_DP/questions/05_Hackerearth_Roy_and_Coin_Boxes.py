def main():
    n = int(input())
    f = [0] * (n + 1)
    m = int(input())
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    
    for _ in range(m):
        L, R = map(int, input().split())
        l[L] += 1
        r[R] += 1
    
    f[1] = l[1]
    for i in range(2, n + 1):
        f[i] = l[i] - r[i - 1] + f[i - 1]
    
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

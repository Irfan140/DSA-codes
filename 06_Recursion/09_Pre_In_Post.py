def pip(n):
    if n == 0:
        return
    print(f"Pre {n}")
    pip(n - 1)
    print(f"In {n}")
    pip(n - 1)
    print(f"Post {n}")

def main():
    pip(3)

if __name__ == "__main__":
    main()

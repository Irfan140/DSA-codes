def main():
    # taking input when size is not mentioned earlier
    v = []
    print("Enter elements: ", end="")
    for i in range(5):
        x = int(input())
        v.append(x)
    
    for i in range(5):
        print(v[i], end=" ")

if __name__ == "__main__":
    main()

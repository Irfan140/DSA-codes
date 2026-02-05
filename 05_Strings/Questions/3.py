def main():
    s = "yyyyyhhnj"
    max_count = 0

    # First pass: find max frequency
    for i in range(len(s)):
        count = 1
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                count += 1
        if count > max_count:
            max_count = count

    # Second pass: print characters with max frequency
    for i in range(len(s)):
        count = 1
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                count += 1
        if count == max_count:
            print(s[i], max_count)
            break   # remove this if you want all max chars

if __name__ == "__main__":
    main()
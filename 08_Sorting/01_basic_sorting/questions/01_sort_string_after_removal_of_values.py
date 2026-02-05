# Sort a string in decreasing order of values associated after removal of values smaller than X

def main():
    s = "AZYZXBDXJK"
    str_result = ""
    for i in range(len(s)):
        if s[i] >= 'X':
            str_result += s[i]
    str_result = ''.join(sorted(str_result))
    print(str_result)

if __name__ == "__main__":
    main()

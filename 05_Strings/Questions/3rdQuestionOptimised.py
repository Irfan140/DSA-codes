"""Converted from 3rdQuestionOptimised.cpp — original C++ removed."""

def main():
    s = "Irfannnn"
    s = s.lower()
    arr = [0] * 26
    for ch in s:
        if 'a' <= ch <= 'z':
            arr[ord(ch) - 97] += 1
    mx = max(arr)
    for i in range(26):
        if arr[i] == mx:
            ch = chr(i + 97)
            print(ch, mx)

if __name__ == "__main__":
    main()

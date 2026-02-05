"""Converted from 4.cpp — original C++ removed."""

def main():
   from collections import Counter

   s = "Irfan Mehmud is a boy. He is also a man"
   words = s.split()
   cnt = Counter(words)
   most_common_word, freq = cnt.most_common(1)[0]
   print(most_common_word, freq)

if __name__ == "__main__":
    main()

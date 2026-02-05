
def main():
    # Strings in Python are immutable, so many operations return a NEW string instead of modifying in-place.

    # string length
    # str = "Irfan"
    # print(len(str))   # does not count null character (same as C++)

    # push elements
    # str = str + 'e'   # only one character
    # print(str)

    # pop elements
    # str = str[:-1]
    # print(str)


    # + operator (string concatenation)

    # x = "Irfan "
    # y = "Mehmud"

    # x += y
    # print(x)

    # x += " is a student"  # + operator used for modify
    # print(x)


    # reverse full string
    # str = "Irfan"
    # str = str[::-1]
    # print(str)


    

    str = "Irfan"

    # reverse from index 1 to index 3 (Python slicing end is exclusive)
    # Python: reverse str[1:4]

    reversed_part = str[1:4][::-1]
    print(reversed_part)
    str = str[0:1] + reversed_part + str[4:]

    print(str)

if __name__ == "__main__":
    main()

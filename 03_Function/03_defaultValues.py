def fun(x=7, y=8):
    # 7 is now default value of x
    # 8 is now default value of y
    # we must give default values to all arguments, if not then will get error
    print(x, y)

def main():
    fun()  # now if we pass any values here it will not affect the default values

if __name__ == "__main__":
    main()

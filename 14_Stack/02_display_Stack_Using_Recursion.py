def displayRec(st):
    if len(st) == 0:
        return
    x = st[-1]
    print(x, end=" ")
    st.pop()
    displayRec(st)
    # print(x, end=" ")  #! use this for normal display
    st.append(x)


def main():
    st = []
    st.append(1)
    st.append(2)
    st.append(3)
    st.append(4)
    displayRec(st)


if __name__ == "__main__":
    main()

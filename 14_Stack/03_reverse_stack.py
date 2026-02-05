def print_stack(st):
    temp = []
    while len(st) > 0:
        print(st[-1], end=" ")
        temp.append(st[-1])
        st.pop()
    while len(temp) > 0:
        st.append(temp[-1])
        temp.pop()
    print()


def main():
    st = []
    st.append(1)
    st.append(2)
    st.append(3)
    st.append(4)

    temp = []
    while len(st) > 0:
        temp.append(st[-1])
        st.pop()

    temp1 = []
    while len(temp) > 0:
        temp1.append(temp[-1])
        temp.pop()

    while len(temp1) > 0:
        st.append(temp1[-1])
        temp1.pop()

    print_stack(st)


if __name__ == "__main__":
    main()

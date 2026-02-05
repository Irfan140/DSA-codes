def pushAtBottom(st, val):
    temp = []
    while len(st) > 0:
        temp.append(st[-1])
        st.pop()
    st.append(val)
    while len(temp) > 0:
        st.append(temp[-1])
        temp.pop()


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


def reverseStack(st):
    if len(st) == 1:
        return
    x = st[-1]
    st.pop()
    reverseStack(st)
    pushAtBottom(st, x)


def main():
    st = []
    st.append(1)
    st.append(2)
    st.append(3)
    st.append(4)
    reverseStack(st)
    print_stack(st)


if __name__ == "__main__":
    main()

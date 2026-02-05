def main():
    st = []
    st.append(1)
    st.append(2)
    st.append(3)
    st.append(100)
    
    # printing stack element in reverse order...
    temp = []
    while len(st) > 0:
        print(st[-1])
        temp.append(st[-1])
        st.pop()
        
    while len(temp) > 0:
        st.append(temp[-1])
        temp.pop()

if __name__ == "__main__":
    main()

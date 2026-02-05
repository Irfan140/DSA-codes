
def display_stack(stack):
    temp = []
    while len(stack) > 0:
        print(stack[-1])
        temp.append(stack[-1])
        stack.pop()

    while len(temp) > 0:
        stack.append(temp[-1])
        temp.pop()


def addAtIndex(stack, idx, val):
    temp = []

    while len(stack) > idx:
        temp.append(stack[-1])
        stack.pop()

    stack.append(val)

    while len(temp) > 0:
        stack.append(temp[-1])
        temp.pop()
    

def main():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)

    display_stack(stack)

    addAtIndex(stack, 2, 100)

    display_stack(stack)

if __name__ == "__main__":
    main()
class A:
    def __init__(self):
        self.a_ka_public = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.b_ka_public = 0


class C(A):
    def __init__(self):
        super().__init__()
        self.c_ka_public = 0


class D(B, C):
    def __init__(self):
        super().__init__()   # MRO ensures A is called once
        self.d_ka_public = 0

    def show(self):
        print(self.a_ka_public)   # only one A instance


def main():
    d = D()
    d.a_ka_public = 10
    d.show()


if __name__ == "__main__":
    main()

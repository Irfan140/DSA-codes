class Vehicle:   # base class, parent class
    def __init__(self):
        self.tyreSize = 0
        self.engineSize = 0
        self.lights = 0
        self.companyName = ""


class Bike(Vehicle):   # derived class, child class
    def __init__(self):
        super().__init__()   # call Vehicle constructor
        self.handleSize = 0


def main():
    honda = Bike()
    honda.handleSize = 5
    honda.engineSize = 10
    honda.companyName = "honda"

    print(honda.handleSize)


if __name__ == "__main__":
    main()

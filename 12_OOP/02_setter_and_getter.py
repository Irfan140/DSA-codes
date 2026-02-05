class Player:
    def __init__(self):
        self._score = 0
        self._health = 0

    # setters
    def setScore(self, s):
        self._score = s

    def setHealth(self, h):
        self._health = h

    # getters
    def getScore(self):
        return self._score

    def getHealth(self):
        return self._health


def main():
    amit = Player()
    amit.setHealth(199)
    print(amit.getHealth())


if __name__ == "__main__":
    main()

class Player:
    def __init__(self):
        self._health = 0
        self._age = 0
        self._score = 0
        self._alive = False

    # getters
    def getHealth(self):
        return self._health

    def getAge(self):
        return self._age

    def getScore(self):
        return self._score

    def getIsAlive(self):      # FIXED name
        return self._alive

    # setters
    def setHealth(self, health):
        self._health = health

    def setAge(self, age):
        self._age = age

    def setScore(self, score):
        self._score = score

    def setIsAlive(self, alive):
        self._alive = alive


# function: add scores of two players
def addScore(a: Player, b: Player):
    return a.getScore() + b.getScore()


# function: return player with max score
def maxScore(a: Player, b: Player):
    if a.getScore() > b.getScore():
        return a
    else:
        return b


def main():
    harsh = Player()
    raghav = Player()

    harsh.setAge(20)
    harsh.setHealth(100)
    harsh.setIsAlive(True)
    harsh.setScore(25)

    raghav.setAge(10)
    raghav.setHealth(150)
    raghav.setIsAlive(False)
    raghav.setScore(50)

    print(addScore(harsh, raghav))

    sanket = maxScore(harsh, raghav)
    print(sanket.getScore())
    print()

    # C++ dynamic memory equivalent
    urvi = Player()        # no pointers needed in Python
    urviObject = urvi     # reference copy

    urviObject.setAge(100)
    print(urviObject.getAge())


if __name__ == "__main__":
    main()

class Player:
    def __init__(self):
        self.score = 0  # data member
        self.health = 0 # data member
        
    # member method
    def show_health(self):
        print(self.health)

def main():

    # amit is a reference to an object of class Player.
    amit = Player()  
    amit.score = 90
    amit.health = 100
    
    print(amit.health)
    amit.show_health()

if __name__ == "__main__":
    main()

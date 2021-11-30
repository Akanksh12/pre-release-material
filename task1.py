class Player:
    def __init__(self, name, scoreList):
        self.name = name
        self.scoreList = []

# taking in number of players

numberOfPlayers = int(input("How many players are there?(2,3,4)\n"))
players = []
if numberOfPlayers > 2 and numberOfPlayers < 5:
    print("You have entered an invalid input, please input only 2,3 or 4")

# taking the name of the players

for i in range(numberOfPlayers):
    name = str(input(f"What is the name of player:{i+1}\n"))
    globals()[f'{name}'] = Player(name,[])
    players.append(globals()[f'{name}'])

# taking in number of holes to be played

try:
    numberOfHoles = int(input("Enter the number of holes to be played\n"))
except:
    print("Please enter a valid integer(9 or 18)")

# taking the par 

try:
    par = int(input("Enter the par"))
except:
    print("Enter a valid response, only a integer")



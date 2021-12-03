class Player:
    def __init__(self, name, scoreList):
        self.name = name
        self.scoreList = []

# taking in number of players

numberOfPlayers = int(input("How many players are there?(2,3,4)\n"))
players = []
if numberOfPlayers < 2 or numberOfPlayers > 4:
    print("You have entered an invalid input, please input only 2,3 or 4")
    quit()

# taking the name of the players

for i in range(numberOfPlayers):
    name = str(input(f"What is the name of player:{i+1}\n"))
    for i in range(len(name)):
        if name[i].isdigit():
            print("The name is not valid")
            quit()
    print(name)
    name = Player(name,[])
    print(name)
    players.append(name)

# taking in number of holes to be played
numberOfHoles = int(input("Enter the number of holes to be played\n"))
if numberOfHoles == 9 or numberOfHoles == 18:
    print("You have entered a valid input")
else:
    print("You have entered an invalid input, please enter 9 or 18")
# taking the par 

try:
    par = int(input("Enter the par\n"))
except:
    print("Enter a valid response, only a integer")

print(f'The number of players are: {numberOfPlayers}')
print("Names of the players are:")
for i in range(len(players)):
    print(f"player:{i + 1} : {players[i].name}")

print("number of pholes to be played:", numberOfHoles)
print("par:", par)



class Player:
    def __init__(self, name, scoreList):
        self.name = name
        self.scoreList = []

numberOfPlayers = int(input("How many players are there?(2,3,4)\n"))
if numberOfPlayers > 2 and numberOfPlayers < 5:
    continue
else:
    print("You have entered an invalid input, please input only 2,3 or 4")



#task 1
class Player:
    def __init__(self, name, scoreList):
        self.name = name
        self.scoreList = []

# taking in number of players
while True:
    numberOfPlayers = int(input("How many players are there?(2,3,4)\n"))
    players = []
    if numberOfPlayers < 2 or numberOfPlayers > 4:
        print("You have entered an invalid input, please input only 2,3 or 4")
    else:
        break

# taking the name of the players

for i in range(numberOfPlayers):
    try:
        name = str(input(f"What is the name of player:{i+1}\n"))
    except:
        print("Please enter a valid name(do not include numbers")
        break

    for j in range(len(name)):
        if name[i].isdigit():
            print("The name is not valid")
        else:
            name = Player(name, [])
            players.append(name)
            break
           
# taking in number of holes to be played
while True:
    numberOfHoles = int(input("Enter the number of holes to be played\n"))
    if numberOfHoles == 9 or numberOfHoles == 18:
        print("You have entered a valid input")
        break
    else:
        print("You have entered an invalid input, please enter 9 or 18")

for i in range(len(players)):
    for j in range(numberOfHoles):
        players[i].scoreList.append(0)
# taking the par 
try:
    while True:
        par = int(input("Enter the par\n"))
        if par < numberOfHoles:
            print("Please enter a integer above the number of holes specified")
        else:
            break
except:
    print("Enter a valid response, only a integer")

#displaying all the data taken 

print(f'The number of players are: {numberOfPlayers}')
print("Names of the players are:")
for i in range(len(players)):
    print(f"player:{i + 1} : {players[i].name}")

print("number of pholes to be played:", numberOfHoles)
print("par:", par)

# task 2

# taking in scores of players

for i in range(numberOfHoles):
    j = 0
    while j <= (numberOfPlayers - 1):
        try:
            score1 = int(input(f"Enter the score for hole {i + 1}, of player {players[j].name} (first time)\n"))
            score2 = int(input(f"Enter the score for hole {i + 1}, of player {players[j].name} (second time)\n"))
            scores = [score1, score2]
        except:
            print("Input is invalid, please enter a valid integer not a string")
        for x in range(len(scores)):
            if scores[x] < 0:
                print(f"score {x} is a invalid input(value is less than 0), please enter a integer above -1")
                continue
        if score1 == score2:
            print("Both the inputs are the same")
            players[j].scoreList[i] = score1
            j += 1
        else:
            print(f"{score1} and {score2} are not the same. Please enter your score again")

# asking for which player to display their scores
while True:
    try:
        showScores = str(input("Would you like to view any players scores?(Y or N)\n"))
        if showScores == "Y" or showScores == "y":
            playern = str(input(f"Enter the player's name\n"))
            for i in range(numberOfPlayers):
                if players[i].name == playern:
                    playern = i
                    break
            print(f"{players[playern].name}'s scores are:")
            for i in range(numberOfHoles):
                print(f"score for hole {i + 1} is {players[playern].scoreList[i]}")
            break
        else:
            break
    except:
        print("Please enter Y or N")

# task 3

# displaying scores relative to par

print("\n\nName\tscore")
scores = []
for i in range(numberOfPlayers):
    score = sum(players[i].scoreList)
    scores.append(score)
    scoreRelativeToPar = score - par
    if scoreRelativeToPar < 0:
        scoreRelativeToPar *= -1
        print(f"{players[i].name}\t{scoreRelativeToPar} under par")
    else:
        print(f"{players[i].name}\t{scoreRelativeToPar} over par")

scores.sort()
for i in range(len(players)):
    currentScore = sum(players[i].scoreList)
    if scores[i] == currentScore:
        winner = players[i].name

print(f"Winner is {winner} with the score of {scores[0]}")

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
    for j in range(len(players)):
        score = int(input(f"Enter the score for hole {i + 1} by {players[j].name}"))
        score2 = int(input(f"Enter the score for hole {i + 1} by {players[j].name}, again for confirmation"))
        scores = [score, score2]
        try:
            for i in range(scores):
                if scores[i] < 0:
                    print(f"{scores[i]} is a invalid score,please enter a positive integer")
                    continue
                else:
                    break
        except:
            print("The score entered is invalid, please enter only a positive integer")

        print("the scores entered are:", score, score2)
        if score == score2:
            print("The scores are the same")
        else:
            print("The scores are not the same please try again")
        
playern = int(input(f"Enter your player number for checking your scores(1,2,3 or 4)"))
playern -= 1
print(f"{players[playern].name}'s scores are:")
for i in range(numberOfHoles):
    print(f"score for hole {i + 1} is {players[playern].scoreList[i]}")



    


            







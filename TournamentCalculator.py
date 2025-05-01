diction = {}
choice = "yes"
while(choice == "yes"):
    choice = ""

    players = int(input("How many players are playing? "))
    for i in range(players):
        name = input(f"Player {i+1} name: ")
        diction[name] = []
        
    courses = int(input("How many courses are you racing? "))

    for i in range(courses):
        print(f"\nRound {i+1}")
        for j in diction:
            score = int(input(f"What is {j}'s score? "))
            diction[j].append(score)

    with open("KartScores.txt", "a") as f:
        #adds player name and scores to a string and puts it in the file
        for i in diction:
            newLine = ""
            sum = 0
            for j in diction[i]:
                newLine += str(j) + " "
                sum += j
            f.write(f"{i} scores: {newLine}\n")
            f.write(f"\tAverage: {sum / len(diction[i])}\n")

    while(choice != "yes" and choice != "no"):
        choice = (input("Would you like to start again? ")).lower()
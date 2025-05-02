def gameNum():
    game = 0
    with open("KartScores.txt", "r") as file:
        for line in file:
            if is_indented(line):
                pass
            else:
                num = int(line)
                if num > game:
                    game = num        
    return game

def is_indented(line):
    return len(line) - len(line.lstrip()) > 0



if __name__ == "__main__":
    choice = "yes"
    game = gameNum()

    while(choice == "yes"):
        game += 1
        scoreDiction = {}
    
        choice = ""

        players = int(input("How many players are playing? "))
        for i in range(players):
            name = input(f"Player {i+1} name: ")
            scoreDiction[name] = []
        
        courses = int(input("How many courses are you racing? "))

        for i in range(courses):
            print(f"\nRound {i+1}")
            for j in scoreDiction:
                score = int(input(f"How many points did {j} gain? "))
                scoreDiction[j].append(score)

        totalDiction = {}
        with open("KartScores.txt", "a") as f:
            f.write(f"{game}\n")
            #adds player name and scores to a string and puts it in the file
            for i in scoreDiction:
                newLine = ""
                sum = 0
                for j in scoreDiction[i]:
                    newLine += str(j) + " "
                    sum += j
                    totalDiction[i] = sum
            
                f.write(f"\t{i} scores: {newLine}\n")
                f.write(f"\t\tTotal Score: {sum}\n")
                f.write(f"\t\tAverage: {sum / len(scoreDiction[i])}\n")

            max = 0
            maxName = []
            for i in totalDiction:
                if totalDiction[i] > max:
                    max = totalDiction[i]
                    maxName = [i]
                elif totalDiction[i] == max:
                    maxName.append(i)

            if len(maxName) > 1:
                f.write(f"\t\tWinners: {", ".join(maxName)} Points: {max}\n")
            else:
                f.write(f"\tWinner: {maxName[0]} Points: {max}\n")

        while(choice != "yes" and choice != "no"):
            choice = (input("Would you like to start again? ")).lower()

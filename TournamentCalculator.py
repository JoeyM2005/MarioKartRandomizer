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
        diction = {}
    
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
            f.write(f"{game}\n")
            #adds player name and scores to a string and puts it in the file
            for i in diction:
                newLine = ""
                sum = 0
                for j in diction[i]:
                    newLine += str(j) + " "
                    sum += j
            
                f.write(f"\t{i} scores: {newLine}\n")
                f.write(f"\t\tAverage: {sum / len(diction[i])}\n")

        while(choice != "yes" and choice != "no"):
            choice = (input("Would you like to start again? ")).lower()
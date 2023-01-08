f = open("02/input.txt", "r")
input = []

# Values given by exercise description

# Rock = A or X 1pt
# Paper = B or Y 2pts
# Scissors = C or Z 3pts

# For part two:
# X lose
# Y draw
# Z win

# Win = 6pts
# Draw = 3pts
# Lose = 0pts

# Read file with strip to remove "\n"
for line in f:
    line = line.strip()
    round = [line[0], line[-1]]
    input.append(round)
    
# For part one
def checkRound(round):
    if round[1] == "X":
        if round[0] == "A":
            return 4
        elif round[0] == "B":
            return 1
        elif round[0] == "C":
            return 7
    elif round[1] == "Y":
        if round[0] == "A":
            return 8
        elif round[0] == "B":
            return 5
        elif round[0] == "C":
            return 2
    elif round[1] == "Z":
        if round[0] == "A":
            return 3
        elif round[0] == "B":
            return 9
        elif round[0] == "C":
            return 6

# For part two
def checkRound2(round):
    if round[1] == "X":
        if round[0] == "A":
            return 3
        elif round[0] == "B":
            return 1
        elif round[0] == "C":
            return 2
    elif round[1] == "Y":
        if round[0] == "A":
            return 4
        elif round[0] == "B":
            return 5
        elif round[0] == "C":
            return 6
    elif round[1] == "Z":
        if round[0] == "A":
            return 8
        elif round[0] == "B":
            return 9
        elif round[0] == "C":
            return 7
        
pointsPart1 = 0
pointsPart2 = 0

for round in input:
    pointsPart1 += checkRound(round)
    pointsPart2 += checkRound2(round)
    
print(pointsPart1)
print(pointsPart2)
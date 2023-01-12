f = open("04/input.txt", "r")
input = []

# Read file with strip to remove "\n"
for line in f:
    line = line.strip()
    # Elves ranges as strings
    pair = line.split(",")
    # Elf 1 range as integers
    elf1 = (int(pair[0].split("-")[0]), int(pair[0].split("-")[1]))
    # Elf 2 range as integers
    elf2 = (int(pair[1].split("-")[0]), int(pair[1].split("-")[1]))
    # Elves ranges as tuple of tuples
    input.append((elf1, elf2))

# Part 1
sum1 = 0

def checkRanges(elf1: range, elf2: range) -> bool:
    return (elf1.start in elf2 and elf1.stop - 1 in elf2) or (elf2.start in elf1 and elf2.stop - 1 in elf1)

# Part 2
sum2 = 0

def checkOverlap(elf1: range, elf2: range) -> bool:
    for i in elf1:
        if i in elf2:
            return True

for pair in input:
    elf1 = range(pair[0][0], pair[0][1] + 1)
    elf2 = range(pair[1][0], pair[1][1] + 1)
    if checkRanges(elf1, elf2):
        sum1 += 1
    if checkOverlap(elf1, elf2):
        sum2 += 1

print(sum1)
print(sum2)
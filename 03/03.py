f = open("03/input.txt", "r")
input = []

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Read file with strip to remove "\n"
for line in f:
    line = line.strip()
    input.append(line)

# Part 1
sum1 = 0

for ruckshack in input:
    c1 = ruckshack[0:len(ruckshack)//2]
    c2 = ruckshack[len(ruckshack)//2:len(ruckshack)]
    for item in c1:
        if item in c2:
            sum1 += letters.index(item) + 1
            break
        
print(sum1)

# Part 2
sum2 = 0

for i in range(0, len(input), 3):
    elf1 = input[i]
    elf2 = input[i+1]
    elf3 = input[i+2]
    for item in elf1:
        if item in elf2 and item in elf3:
            sum2 += letters.index(item) + 1
            break
    
print(sum2)
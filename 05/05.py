import copy

f = open("05/input.txt", "r")

movements = []
stacks1 = {}
    
for line in f:
    length = len(line)
    # Check if line is empty
    if length == 1:
        pass
    # Get stacks of crates
    if "[" in line:
        col = 1
        for i in range(1, length, 4):
            if line[i].isalpha():
                if col in stacks1.keys():
                    # Since file reads stacks from top to bottom here crate is added in bottom of stack (first index of list)
                    stacks1[col].insert(0, line[i])
                else:
                    stacks1[col] = [line[i]]
            col += 1
    # Get crates movements
    elif "move" in line:
        l = line.strip().split(" ")
        # First item is number of crates
        # Second item is "from" stack
        # Third item is "to" stack
        movements.append([int(l[1]), int(l[3]), int(l[5])])

# Creates deep copy of a dictionary so iterable objects in both dictionaries will be independent
stacks2 = copy.deepcopy(stacks1)

# For part 1
for m in movements:
    for number in range(m[0]):
        stacks1[m[2]].append(stacks1[m[1]].pop())
        
result1 = ""

for s in range(1, len(stacks1) + 1):
    result1 += stacks1[s][-1]
        
print(result1)

# For part 2
for m in movements:
    cratesToMove = []
    for number in range(m[0]):
        cratesToMove.insert(0, stacks2[m[1]].pop())
    stacks2[m[2]] += cratesToMove
    
result2 = ""

for s in range(1, len(stacks2) + 1):
    result2 += stacks2[s][-1]
        
print(result2)
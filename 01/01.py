f = open("01/input.txt", "r")
input = []

for line in f:
    line = line.strip()
    input.append(int(line)) if line.isdigit() else input.append("")
    
# Extra append to trigger else block to check last value position in top 3
input.append("")
    
maxCals1 = 0
maxCals2 = 0
maxCals3 = 0
elfCals = 0

for item in input:
    if type(item) == int:
        elfCals += int(item)
    else:
        if elfCals > maxCals1:
            maxCals3 = maxCals2
            maxCals2 = maxCals1
            maxCals1 = elfCals
        elif maxCals1 > elfCals > maxCals2:
            maxCals3 = maxCals2
            maxCals2 = elfCals
        elif maxCals2 > elfCals > maxCals3:
            maxCals3 = elfCals
        elfCals = 0

print(maxCals1)
print(maxCals1 + maxCals2 + maxCals3)
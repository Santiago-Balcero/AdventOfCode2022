f = open("06/input.txt", "r")

datastream = f.readline()

# For part 1
for i in range(3, len(datastream)):
    # Length of set of characters from substring must equal 4 to identify the start-of-packet marker
    if len(set([*datastream[i-3:i+1]])) == 4:
        print(i+1)
        break
    
# For part 2
for i in range(13, len(datastream)):
    # Length of set of characters from substring must equal 14 to identify the start-of-message marker
    if len(set([*datastream[i-13:i+1]])) == 14:
        print(i+1)
        break
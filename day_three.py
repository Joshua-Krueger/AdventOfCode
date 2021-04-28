import math

with open("d3Data.txt", 'r') as f:  # Opens the data to look at
    lines = f.read().splitlines()  # Splits the data into the correct format for the problem

routes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))  # All the spots needed to be looked at for the path

total = []  # to keep track outside of the loop
for route in routes:  # Loop to look at each position
    count = 0  # Counter
    for v in range(0, len(lines), route[1]):  # for loop to look at each position starting from zero, ending at the end, and incrementing by route
        h = int(divmod((v / route[1]) * route[0], len(lines[v]))[1])  # returns quotient and remainder, finding where it is
        value = lines[v][h]  # finds the character at the position using the tuple and the current spot in the loop
        if value == "#":  # Increment by one if the char at the position is a #
            count += 1
    total.append(count) # adds the count to the total list

print("Solution 1 =>", total[1]) # Gives the number of #s
print("Solution 2 =>", math.prod(total))  # Multiplies all of the values together
input = r"C:\Users\Jens\AdventOfCode\advent-of-code-22\advent-of-code-23\Inputs\day2input.txt"

reader = open(input, 'r')

# A, X = Rock
# B, Y = Paper
# C, Z = Scissors

# X = Lose, Y = Draw, Z = Win
#rock = 1, paper = 2, scissors = 3

pointDict1 = {
    "AX": 0 + 3,
    "AY": 3 + 1,
    "AZ": 6 + 2,
    "BX": 0 + 1,
    "BY": 3 + 2,
    "BZ": 6 + 3,
    "CX": 0 + 2,
    "CY": 3 + 3,
    "CZ": 6 + 1
}

pointDict2 = {
    "AX": 0 + 3,
    "AY": 3 + 1,
    "AZ": 6 + 2,
    "BX": 0 + 1,
    "BY": 3 + 2,
    "BZ": 6 + 3,
    "CX": 0 + 2,
    "CY": 3 + 3,
    "CZ": 6 + 1
}

points1 = 0
points2 = 0

for line in reader.readlines():
    a1 = pointDict1[line.replace(" ", "").strip()]
    a2 = pointDict2[line.replace(" ", "").strip()]
    points1 += int(a1)
    points2 += int(a2)

print("first method gives: " + str(points1))
print("second method gives: " + str(points2))
 
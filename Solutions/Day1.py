#Solush goes here
input: str = r"C:\Users\Jens\AdventOfCode\advent-of-code-22\advent-of-code-23\Inputs\day1input.txt"
reader = open(input, "r")

i = 0
list = []
line = reader.readline()

while line:
    if line.strip() != "":
        i += int(line)
    else:
        list.append(i)
        i = 0
    line = reader.readline()
print("the elf with the most food has " + str(max(list)) + "calories worth of food.")

list.sort(reverse=True)
sum = sum(list[0:3])
print("The top 3 elves have " + str(sum) + "calories")
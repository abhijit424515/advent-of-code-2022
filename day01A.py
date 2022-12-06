f = open("day01_input", "r")

topper = 0
player = 0

for line in f:
    if line.strip() == "":
        topper = max(topper, player)
        player = 0
    else:
        player += int(line.strip())

print(topper)

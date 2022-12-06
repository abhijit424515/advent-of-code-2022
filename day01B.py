f = open("day01_input", "r")

totals = []
player = 0

for line in f:
    if line.strip() == "":
        totals.append(player)
        player = 0
    else:
        player += int(line.strip())

totals.sort(reverse=True)
final = 0
for i in range(min(3, len(totals))):
    final += totals[i]

print(final)

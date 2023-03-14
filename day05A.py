from functools import reduce
f = open("day05_input", "r")

data = []
steps = []

switch = False
for x in f:
    line = x.strip()
    if line != "":
        if (switch):
            steps.append(line)
        else:
            data.append([i for i in x][1::4])
    else:
        switch = True

crates = [list(filter(lambda x: x != " ", i))[
    ::-1] for i in zip(*data[0:-1])]
moves = [[int(j) for j in i.split(" ")[1::2]] for i in steps]

for move in moves:
    crates[move[2]-1] = crates[move[2]-1] + \
        crates[move[1]-1][(-move[0]):][::-1]
    crates[move[1]-1] = crates[move[1]-1][:(-move[0])]

print(crates)

final = reduce(lambda x, y: x+y, [x[-1] for x in crates])
print(final)

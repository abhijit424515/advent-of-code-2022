f = open("day03_input", "r")

score = 0

for x in f:
    line = x.strip()
    intersect = set(list(line[:(len(line)//2)])
                    ).intersection(list(line[(len(line)//2):]))
    score += (lambda x: x-38 if x <= 90 else x-96)(ord(list(intersect)[0]))

print(score)

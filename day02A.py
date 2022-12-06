f = open("day02_input", "r")

sum = 0
for line in f:
    match line.strip():
        case "A X":
            sum += 1+3
        case "A Y":
            sum += 2+6
        case "A Z":
            sum += 3+0
        case "B X":
            sum += 1+0
        case "B Y":
            sum += 2+3
        case "B Z":
            sum += 3+6
        case "C X":
            sum += 1+6
        case "C Y":
            sum += 2+0
        case "C Z":
            sum += 3+3

print(sum)

file = open('day06_input', 'r')

s = []
i = 1

while True:
    if len(s) == 14:
        break

    char = file.read(1)
    if not char:
        break

    if char not in s:
        s.append(char)
    else:
        s = s[s.index(char)+1:]
        s.append(char)

    i += 1

file.close()

print(i-1)

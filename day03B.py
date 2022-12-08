import string
f = open("day03_input", "r")

common = set(string.ascii_letters)
score = 0
index = 0

for x in f:
    line = x.strip()
    common = common.intersection(set(list(line)))

    if (index == 2):
        score += (lambda x: x-38 if x <= 90 else x-96)(ord(list(common)[0]))
        common = set(string.ascii_letters)
    index = (index+1) % 3

print(score)

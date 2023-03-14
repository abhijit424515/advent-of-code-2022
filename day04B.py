f = open("day04_input", "r")

count = 0

for x in f:
    arr = [[int(j) for j in i.split("-")] for i in x.strip().split(",")]
    if not (arr[0][1]<arr[1][0] or arr[1][1]<arr[0][0]):
      count += 1

print(count)

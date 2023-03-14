f = open("day04_input", "r")

count = 0

for x in f:
    arr = [[int(j) for j in i.split("-")] for i in x.strip().split(",")]
    if ((arr[0][0]>=arr[1][0] and arr[0][1] <= arr[1][1]) or (arr[0][0]<=arr[1][0] and arr[0][1] >= arr[1][1])):
      count += 1

print(count)

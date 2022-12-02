# f = open("small_input.txt", "r")
f = open("input.txt", "r")

carries = []
total = 0

for line in f.readlines():
  if line != "\n":
    num = int(line.strip())
    total += num
  else:
    carries.append(total)
    total = 0

carries.append(total)
carries.sort()
print("First:", carries[-1])
print(sum("Second:", carries[-3:]))

f.close()
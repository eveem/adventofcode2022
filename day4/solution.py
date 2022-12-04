# f = open("small_input.txt", "r")
f = open("input.txt", "r")

total_1 = 0
total_2 = 0

for line in f.readlines():
  p1, p2 = line.strip().split(",")
  s1, e1 = map(int, p1.split("-"))
  s2, e2 = map(int, p2.split("-"))

  p1 = set(range(s1, e1 + 1))
  p2 = set(range(s2, e2 + 1))

  t = len(p1.union(p2))
  if t == len(p1) or t == len(p2):
    total_1 += 1
  
  i = len(p1.intersection(p2))
  if i > 0:
    total_2 += 1

print(total_1)
print(total_2)
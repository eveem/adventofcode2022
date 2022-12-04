mapper = {}

for i in range(26):
  mapper[chr(ord("a") + i)] = i + 1

for i in range(26):
  mapper[chr(ord("A") + i)] = i + 1 + 26

# f = open("small_input.txt", "r")

def first_part(filename):
  f = open(filename, "r")

  total = 0

  for line in f.readlines():
    line = line.strip()
    n = len(line)
    mid = n // 2

    first = set(line[:mid])
    second = set(line[mid:])

    both = first.intersection(second).pop()
    total += mapper[both]

  f.close()
  return total

def second_part(filename):
  f = open(filename, "r")

  total = 0
  counter = 0
  temp = set()

  for line in f.readlines():
    line = line.strip()

    if counter == 0:
      temp = set(line)
      counter += 1
    elif counter == 1:
      temp = temp.intersection(set(line))
      counter += 1
    elif counter == 2:
      temp = temp.intersection(set(line))
      common = temp.pop()
      total += mapper[common]
      counter = 0
  
  return total

print(first_part("small_input.txt"))
print(first_part("input.txt"))
print(second_part("small_input.txt"))
print(second_part("input.txt"))
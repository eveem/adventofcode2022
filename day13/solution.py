from ast import literal_eval

# f = open("small_input.txt")
f = open("input.txt")
lines = [line.strip() for line in f.readlines()]
n = len(lines)
pair = 1
total = 0

def cmp(left, right):
  if left == right:
    return "eq"
  elif isinstance(left, int) and isinstance(right, int):
    return left < right
  elif isinstance(left, int) and isinstance(right, list):
    return cmp([left], right)
  elif isinstance(left, list) and isinstance(right, int):
    return cmp(left, [right])
  elif isinstance(left, list) and isinstance(right, list):
    for l, r in zip(left, right):
      status = cmp(l, r)
      if status != "eq":
        return status
    return cmp(len(left), len(right))
  
for i in range(0, n, 3):
  left = literal_eval(lines[i])
  right = literal_eval(lines[i + 1])

  if cmp(left, right):
    total += pair
  pair += 1

print(total)
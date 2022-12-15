from ast import literal_eval
from functools import cmp_to_key
from struct import pack

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

print("PART 1:", total)

packets = [literal_eval(item) for item in lines if item != ""]
packets.append([[2]])
packets.append([[6]])

n = len(packets)

for i in range(n):
  min_idx = i
  for j in range(i + 1, n):
    status = cmp(packets[min_idx], packets[j])
    if status == False:
      min_idx = j
  packets[i], packets[min_idx] = packets[min_idx], packets[i]

expected = open("expected.txt")

# print(all([literal_eval(e.strip()) == p for p, e in zip(packets, expected.readlines())]))

idx2 = packets.index([[2]]) + 1
idx6 = packets.index([[6]]) + 1

# print(idx2, idx6, idx2 * idx6)
print("PART 2:", idx2 * idx6)
import copy

# f = open("small_input_1.txt")
f = open("input.txt")

prev = {"row": 0, "col": 0}
current = {"row": 0, "col": 0}
tail = {"row": 0, "col": 0}

visited = set()

def update_tail(head, tail):
  valid = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, 0)]
  for dx, dy in valid:
    if head["row"] + dx == tail["row"] and head["col"] + dy == tail["col"]:
      return False
  return True

for line in f.readlines():
  direction, step = line.strip().split()
  step = int(step)
  
  for _ in range(step):
    prev = copy.deepcopy(current)
    if direction == "R":  
      current["col"] += 1
    elif direction == "L":
      current["col"] -= 1
    elif direction == "U":
      current["row"] -= 1
    elif direction == "D":
      current["row"] += 1
    
    if update_tail(current, tail):
      tail = copy.deepcopy(prev)
    visited.add((tail["row"], tail["col"]))

print(len(visited))
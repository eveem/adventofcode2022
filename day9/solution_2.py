import copy

# f = open("small_input_1.txt")
f = open("small_input_2.txt")
# f = open("input.txt")

visited = set()
ropes = [[0, 0] for _ in range(10)]

def update_next(prev, next):
  distance = abs(prev[0] - next[0]) + abs(prev[1] - next[1])
  dx, dy = 0, 0
  
  if (prev[0] == next[0] or prev[1] == next[1]) and distance > 1:
    if prev[1] > next[1]:
      dy = 1
    elif prev[1] < next[1]:
      dy = -1
    elif prev[0] > next[0]:
      dx = 1
    elif prev[0] < next[0]:
      dx = -1
  elif (prev[0] != next[0] or prev[1] != next[1]) and distance > 2:
    if prev[0] > next[0] and prev[1] > next[1]:
      dx, dy = 1, 1
    elif prev[0] > next[0] and prev[1] < next[1]:
      dx, dy = 1, -1
    elif prev[0] < next[0] and prev[1] > next[1]:
      dx, dy = -1, 1
    elif prev[0] < next[0] and prev[1] < next[1]:
      dx, dy = -1, -1
  
  return dx, dy

for line in f.readlines():
  direction, step = line.strip().split()
  step = int(step)

  for _ in range(step):
    if direction == "R":
      ropes[0][1] += 1
    elif direction == "L":
      ropes[0][1] -= 1
    elif direction == "U":
      ropes[0][0] -= 1
    elif direction == "D":
      ropes[0][0] += 1

    for i in range(1, 10):
      dx, dy = update_next(ropes[i - 1], ropes[i])
      ropes[i][0] += dx
      ropes[i][1] += dy
      visited.add(tuple(ropes[-1]))

print(len(visited))
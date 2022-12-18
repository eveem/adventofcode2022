from tracemalloc import start
from termcolor import colored
import copy

# f = open("small_input.txt")
f = open("input.txt")
min_x = float("inf")
max_x = float("-inf")
max_y = float("-inf")

paths = []

for line in f.readlines():
  line = line.strip()
  path = line.split("->")
  converted_path = []
  for p in path:
    x, y = map(int, p.strip().split(","))
    converted_path.append([x, y])
    min_x = min(x, min_x)
    max_x = max(x, max_x)
    max_y = max(y, max_y)
  
  paths.append(converted_path)

m = max_y + 1
n = max_x - min_x + 1

grid = [["." for _ in range(n)] for _ in range(m)]

for path in paths:
  prev_x, prev_y = path[0]
  prev_x -= min_x
  grid[prev_y][prev_x] = "#"
  for p in path[1:]:
    dx, dy = p
    curr_x, curr_y = dx - min_x, dy
    
    if curr_x == prev_x:
      for y in range(prev_y, curr_y):
        grid[y][curr_x] = "#"
      for y in range(curr_y, prev_y):
        grid[y][curr_x] = "#"
    
    if curr_y == prev_y:
      for x in range(curr_x, prev_x):
        grid[curr_y][x] = "#"
      for x in range(prev_x, curr_x):
        grid[curr_y][x] = "#"
    
    grid[curr_y][curr_x] = "#"
    prev_x = curr_x
    prev_y = curr_y

start_map = copy.deepcopy(grid)

def drop(x, y):
  visited.add((x, y))
  d.append((x, y))

  if x + 1 < m:
    if (x + 1, y) not in visited and grid[x + 1][y] == ".":
      drop(x + 1, y)
    elif grid[x + 1][y] in "o#":
      if y - 1 >= 0 and (x + 1, y - 1) not in visited and grid[x + 1][y - 1] == ".":
        drop(x + 1, y - 1)
      elif y + 1 < n and (x + 1, y + 1) not in visited and grid[x + 1][y + 1] == ".":
        drop(x + 1, y + 1)

step = 0
while True:
  visited = set()
  d = []
  drop(0, 500 - min_x)
  cx, cy = d[-1]
  if cx + 1 < m and grid[cx + 1][cy] in "o#" and cy - 1 >= 0 and grid[cx + 1][cy - 1] in "o#" and cy + 1 < n and grid[cx + 1][cy + 1] in "o#":
    grid[cx][cy] = "o"
  else:
    break
  step += 1

def show(matrix):
  m = len(matrix)
  n = len(matrix[0])
  for i in range(m):
    for j in range(n):
      if matrix[i][j] == "o":
        print(colored(matrix[i][j], "red"), end="")
      elif matrix[i][j] == "#":
        print(colored(matrix[i][j], "green"), end="")
      else:
        print(matrix[i][j], end="")
    print()

# show(grid)
print("PART 1:", step)

offset = 500
# show(start_map)
for i in range(m):
  start_map[i] = ["." for _ in range(offset)] + start_map[i] + ["." for _ in range(offset)]

n = len(start_map[0])

start_map.append(["." for _ in range(n)])
start_map.append(["#" for _ in range(n)])
# show(start_map)
m = len(start_map)

def drop_2(x, y):
  visited.add((x, y))
  d.append((x, y))

  if x + 1 < m:
    if (x + 1, y) not in visited and start_map[x + 1][y] == ".":
      drop_2(x + 1, y)
    elif start_map[x + 1][y] in "o#":
      if y - 1 >= 0 and (x + 1, y - 1) not in visited and start_map[x + 1][y - 1] == ".":
        drop_2(x + 1, y - 1)
      elif y + 1 < n and (x + 1, y + 1) not in visited and start_map[x + 1][y + 1] == ".":
        drop_2(x + 1, y + 1)

step = 0
prev_x = False
prev_y = False

while True:
  visited = set()
  d = []
  drop_2(0, 500 - min_x + offset)
  cx, cy = d[-1]
  if prev_x == cx and prev_y == cy:
    break
  
  if cx + 1 < m and start_map[cx + 1][cy] in "o#" and cy - 1 >= 0 and start_map[cx + 1][cy - 1] in "o#" and cy + 1 < n and start_map[cx + 1][cy + 1] in "o#":
    start_map[cx][cy] = "o"
  
  step += 1
  prev_x = cx
  prev_y = cy

# show(start_map)
print("PART 2:", step)
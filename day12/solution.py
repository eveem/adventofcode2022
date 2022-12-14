from collections import deque

f = open("small_input.txt")
# f = open("input.txt")

grid = []

for line in f.readlines():
  grid.append(list(line.strip()))

m = len(grid)
n = len(grid[0])

for i in range(m):
  for j in range(n):
    if grid[i][j] == "E":
      target_x = i
      target_y = j
      grid[i][j] = "z"
    
    if grid[i][j] == "S":
      start_x = i
      start_y = j
      grid[i][j] = "a"

q = deque([(start_x, start_y, 0)])
visited = set([(start_x, start_y)])

while q:
  x, y, step = q.popleft()
  if x == target_x and y == target_y:
    print(step)
    break
    
  for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
    if 0 <= dx + x < m and 0 <= dy + y < n and (dx + x, dy + y) not in visited:
      if ord(grid[dx + x][dy + y]) - ord(grid[x][y]) <= 1:
        q.append((dx + x, dy + y, step + 1))
        visited.add((dx + x, dy + y))

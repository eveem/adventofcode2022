# f = open("small_input.txt")
f = open("input.txt")

forest = []

for line in f.readlines():
  forest.append([int(c) for c in line.strip()])

n = len(forest)

top2bottom = [[0 for _ in range(n)] for _ in range(n)]
bottom2top = [[0 for _ in range(n)] for _ in range(n)]
left2right = [[0 for _ in range(n)] for _ in range(n)]
right2left = [[0 for _ in range(n)] for _ in range(n)]

visible = set()

for i in range(n):
  visible.add((i, 0))
  visible.add((0, i))
  visible.add((n - 1, i))
  visible.add((i, n - 1))
  left2right[i][0] = forest[i][0]
  top2bottom[0][i] = forest[0][i]
  bottom2top[n - 1][i] = forest[n - 1][i]
  right2left[i][n - 1] = forest[i][n - 1]

for i in range(n):
  for j in range(1, n):
    if forest[j][i] > top2bottom[j - 1][i]:
      visible.add((j, i))
    top2bottom[j][i] = max(forest[j][i], top2bottom[j - 1][i])

for i in range(n):
  for j in range(n - 2, -1, -1):
    if forest[j][i] > bottom2top[j + 1][i]:
      visible.add((j, i))
    bottom2top[j][i] = max(forest[j][i], bottom2top[j + 1][i])

for i in range(n):
  for j in range(1, n):
    if forest[i][j] > left2right[i][j - 1]:
      visible.add((i, j))
    left2right[i][j] = max(forest[i][j], left2right[i][j - 1])

for i in range(n):
  for j in range(n - 2, -1, -1):
    if forest[i][j] > right2left[i][j + 1]:
      visible.add((i, j))
    right2left[i][j] = max(forest[i][j], right2left[i][j + 1])

def print_map(arr):
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      print(arr[i][j], end=" ")
    print()
  print("-" * 10)

# print_map(forest)
# print("top2bottom")
# print_map(top2bottom)
# print("bottom2top")
# print_map(bottom2top)
# print("left2right")
# print_map(left2right)
# print("right2left")
# print_map(right2left)

print(len(visible))
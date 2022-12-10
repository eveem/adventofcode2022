# f = open("small_input.txt")
f = open("input.txt")

forest = []

for line in f.readlines():
  forest.append([int(c) for c in line.strip()])

n = len(forest)
ans = float("-inf")

for i in range(1, n - 1):
  for j in range(1, n - 1):
    ti = i - 1
    up = 0
    while ti >= 0:
      if forest[ti][j] < forest[i][j]:
        up += 1
      else:
        up += 1
        break
      ti -= 1

    ti = i + 1
    down = 0
    while ti < n:
      if forest[ti][j] < forest[i][j]:
        down += 1
      else:
        down += 1
        break
      ti += 1

    tj = j - 1
    left = 0
    while tj >= 0:
      if forest[i][tj] < forest[i][j]:
        left += 1
      else:
        left += 1
        break
      tj -= 1
    
    tj = j + 1
    right = 0
    while tj < n:
      if forest[i][tj] < forest[i][j]:
        right += 1
      else:
        right += 1
        break
      tj += 1
  
    scenic_score = up * down * left * right
    ans = max(scenic_score, ans)

def print_map(arr):
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      print(arr[i][j], end=" ")
    print()
  print("-" * 10)

print(ans)
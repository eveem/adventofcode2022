from collections import defaultdict

# f = open("small_input.txt" , "r")
f = open("input.txt", "r")

subdirectory = defaultdict(list)
path = []

for line in f.readlines():
  line = line.strip()

  if line[0] == "$":
    if line == "$ cd ..":
      path.pop()
    elif line.startswith("$ cd"):
      dir = line.replace("$ cd ", "")
      path.append(dir)
    elif line.startswith("$ ls"):
      continue
  else:
    if line.startswith("dir"):
      subdirectory["".join(path)].append("".join(path) + line.replace("dir ", ""))
    else:
      subdirectory["".join(path)].append(line)

sizes = defaultdict(int)

while len(sizes) != len(subdirectory):
  for k, v in subdirectory.items():
    if k in sizes:
      continue

    total = 0
    flag = True

    for item in v:
      if item.startswith("/"):
        if item in sizes:
          total += sizes[item]
        else:
          flag = False
          break
      else:
        total += int(item.split(" ")[0])
    
    if flag:
      sizes[k] = total

print(sum(v for k, v in sizes.items() if v <= 100000))

current_space = 70000000 - sizes["/"]
needed = 30000000 - current_space

for space in sorted(sizes.values()):
  if space >= needed:
    print(space)
    break
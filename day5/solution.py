import copy
from collections import defaultdict

# f = open("small_input.txt", "r")
f = open("input.txt", "r")
stacks = defaultdict(list)
second_stacks = defaultdict(list)
mode = "box"

for line in f.readlines():
  if len(line) == 1:
    mode = "cmd"
    for k, v in stacks.items():
      stacks[k] = list(reversed(v))
    second_stacks = copy.deepcopy(stacks)
    continue
  
  if mode == "box":
    n = len(line)
    for i in range(1, n, 4):
      if line[i] >= "A" and line[i] <= "Z":
        stacks[i // 4 + 1].append(line[i])
  elif mode == "cmd":
    line = line.replace("move", "").replace("from", "").replace("to", "")
    m, f, t = map(int, line.split())
    
    for i in range(m):
      x = stacks[f].pop()
      stacks[t].append(x)

    temp = second_stacks[f][-m:]
    second_stacks[f] = second_stacks[f][:-m]
    second_stacks[t] += temp

print("".join(stacks[i][-1] for i in range(1, len(stacks) + 1)))
print("".join(second_stacks[i][-1] for i in range(1, len(second_stacks) + 1)))


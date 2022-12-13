from collections import defaultdict

class Monkey:
  def __init__(self, items, op, num, divisor, tid, fid):
    self.items = items
    self.operate = lambda x: eval(f"x {op} {num}")
    self.divisor = divisor
    self.tid = tid
    self.fid = fid
    self.total = 0

  def __str__(self):
    return f"current items: {self.items}"

  def debug(self):
    print(self.items, self.total)

f = open("small_input.txt")
# f = open("input.txt")

monkeys = defaultdict(int)
id = 0
items = []
op = ""
num = 0
divisor = 1
tid = 0
fid = 0

for line in f.readlines():
  line = line.strip()

  if line.startswith("Monkey"):
    id = int(line.replace(":", "").split()[-1])
  elif "Starting items" in line:
    items = list(map(int, line.split(":")[-1].split(", ")))
  elif "Operation" in line:
    temp = line.split()
    if temp[-1] == "old":
      op = "**"
      num = 2
    else:
      op = temp[-2]
      num = int(temp[-1])
  elif "Test" in line:
    divisor = int(line.split()[-1])
  elif "true" in line:
    tid = int(line.split()[-1])
  elif "false" in line:
    fid = int(line.split()[-1])
  elif len(line) == 0:
    monkeys[id] = Monkey(items, op, num, divisor, tid, fid)

monkeys[id] = Monkey(items, op, num, divisor, tid, fid)

for i in range(20):
  for id in monkeys.keys():
    while monkeys[id].items:
      item = monkeys[id].items.pop(0)
      item = monkeys[id].operate(item)
      item //= 3
      monkeys[id].total += 1
      if item % monkeys[id].divisor == 0:
        monkeys[monkeys[id].tid].items.append(item)
      else:
        monkeys[monkeys[id].fid].items.append(item)
  
  for xx in monkeys.keys():
    print(f"Monkey {xx}: {monkeys[xx]}")
  print("-" * 50)

inspected_count = sorted([monkeys[xx].total for xx in monkeys.keys()])
for xx in monkeys.keys():
  print(f"Monkey {xx}:", monkeys[xx].total)
print("\nPart1:", inspected_count[-1] * inspected_count[-2])
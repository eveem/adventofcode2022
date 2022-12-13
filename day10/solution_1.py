# f = open("example_1.txt")
# f = open("example_2.txt")
f = open("input.txt")

total = 0
cycle = 0
x = 1

def check_cycle(cycle, x):
  if cycle in [20, 60, 100, 140, 180, 220]:
    return x * cycle
  return 0

for line in f.readlines():
  line = line.strip()
  if line == "noop":
    cycle += 1
    total += check_cycle(cycle, x)
  else:
    val = int(line.split()[-1])
    cycle += 1
    total += check_cycle(cycle, x)
    cycle += 1
    total += check_cycle(cycle, x)
    x += val
    
print(total)
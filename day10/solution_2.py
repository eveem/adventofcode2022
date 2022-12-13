# f = open("example_1.txt")
# f = open("example_2.txt")
f = open("input.txt")

cycle = 0
x = 1
ans = ""

def render(cycle, x):
  if cycle % 40 == 39:
    return "\n"
  elif cycle % 40 == x or cycle % 40 == x - 1 or cycle % 40 == x + 1:
    return "# "
  else:
    return ". "

for line in f.readlines():
  line = line.strip()
  if line == "noop":
    ans += render(cycle, x)
    cycle += 1
  else:
    val = int(line.split()[-1])
    ans += render(cycle, x)
    cycle += 1
    ans += render(cycle, x)
    cycle += 1
    x += val

print(ans, end="")
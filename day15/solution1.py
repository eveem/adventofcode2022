from collections import defaultdict

f = open("input.txt")
# f = open("small_input.txt")

sensors = set()
beacons = set()
distance = defaultdict(int)

min_x = float("inf")
max_x = float("-inf")
min_y = float("inf")
max_y = float("-inf")

for line in f.readlines():
  line = line.strip()
  sensor, beacon = line.split(": ")
  sx, sy = map(int, sensor.replace("Sensor at ", "").replace("x=", "").replace("y=", "").split(", "))
  bx, by = map(int, beacon.replace("closest beacon is at ", "").replace("x=", "").replace("y=", "").split(", "))

  sensors.add((sx, sy))
  beacons.add((bx, by))
  distance[(sx, sy)] = abs(bx - sx) + abs(by - sy)
  
  min_x = min(min_x, sx)
  max_x = max(max_x, sx)
  min_y = min(min_y, sy)
  max_y = max(max_y, sy)

md = max(distance.values())  
valid = set()

fy = 10
# fy = 2_000_000

for i in range(min_x - md, max_x + md):
  for sx, sy in sensors:
    if abs(i - sx) + abs(sy - fy) <= distance[(sx, sy)] and (i, fy) not in beacons:
      valid.add((i, fy))

print("PART 1:", len(valid))
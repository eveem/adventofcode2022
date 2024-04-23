from collections import defaultdict
from functools import cache
import re

adj = defaultdict(list)

# input_data = open("small_input.txt").read()
input_data = open("input.txt").read()
data = [[line.split(" ")[1], int(line.split(" ")[4].rstrip(";").replace("rate=", "")), line.split(" ", 9)[-1].split(", ")] for line in input_data.split("\n")]
for org, _, des in data:
  adj[org] = des

cost = defaultdict(int)
for org, c, _ in data:
  cost[org] = c

max_total = 0

@cache
def dfs(node, remain, visited):
  if remain <= 1:
    return 0
  
  result = 0
  for nei in adj[node]:
    result = max(result, dfs(nei, remain - 1, visited))
  if node not in visited and cost[node] > 0:
    visited = tuple(list(visited) + [node])
    result = max(result, dfs(node, remain - 1, visited) + cost[node] * (remain - 1))
  
  return result

print(dfs("AA", 30, ()))
# f = open("small_input.txt", "r")
f = open("input.txt", "r")

mapper = {
  "X": "A", 
  "Y": "B", 
  "Z": "C"
}

shape = {
  "A": 1,
  "B": 2,
  "C": 3
}

win = {
  "A": "B",
  "B": "C",
  "C": "A"
}

lose = {
  "C": "B",
  "B": "A",
  "A": "C"
}

# C > B > A > C

def first_part(f):
  total = 0
  for line in f.readlines():
    opponent, you = line.strip().split()
    you = mapper.get(you)
    total += shape.get(you)

    if opponent == you:
      total += 3
    elif opponent == "C" and you == "A":
      total += 6
    elif opponent == "B" and you == "C":
      total += 6
    elif opponent == "A" and you == "B":
      total += 6
  return total

def second_part(f):
  total = 0
  for line in f.readlines():
    opponent, you = line.strip().split()
    if you == "X":
      total += shape[lose[opponent]]
    elif you == "Y":
      total += 3
      total += shape.get(opponent)
    elif you == "Z":
      total += 6
      total += shape[win[opponent]]
  
  return total

# print(first_part(f))
print(second_part(f))
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

def first_part(opponent, you):
  total = 0
  you = mapper[you]
  total += shape[you]
  
  if opponent == you:
    total += 3
  elif you == win[opponent]:
    total += 6
  
  return total

def second_part(opponent, you):
  total = 0
  
  if you == "X":
    total += shape[lose[opponent]]
  elif you == "Y":
    total += 3
    total += shape.get(opponent)
  elif you == "Z":
    total += 6
    total += shape[win[opponent]]
  
  return total

total_1 = 0
total_2 = 0

for line in f.readlines():
  opponent, you = line.strip().split()

  total_1 += first_part(opponent, you)
  total_2 += second_part(opponent, you)

print("First:", total_1)
print("Second:", total_2)

f.close()
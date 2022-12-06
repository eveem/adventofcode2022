# f = open("small_input.txt", "r")
f = open("input.txt", "r")

s = f.read()
st = []
done = False

for i, c in enumerate(s):
  if len(st) == 4 and done == False:
    print(i)
    done = True
  
  if len(st) == 14:
    print(i)
    break

  while st and c in st:
    st.pop(0)
  st.append(c)
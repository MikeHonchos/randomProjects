ordered = [1,5,2,7,8,3,4]

for i in range(len(ordered) - 1):
  swapped = False
  for j in range(len(ordered) - 1 - i):
    if ordered[j] > ordered[j + 1]:
      ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]
      swapped = True
  if swapped == False:
    break
print(ordered)
import random

def check(comp, user):
  if (comp == user):
    return 0
  if (comp == 0 and user == 1):
    return -1
  if (comp == 1 and user == 2):
    return -1
  if (comp == 2 and user == 0):
    return -1
  return 1
  
comp = random.randint(1, 3)

user = int(input("1 for snake, 2 for water and 3 for gun: "))
score = check(comp, user)

print("\nYou: ", user)
print("computer: ", comp)

if score == 0:
  print("It's a draw")
elif score == -1:
  print("You lose")
else:
  print("You won")
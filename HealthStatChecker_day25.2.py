import random

def diceRoll(sides):
  return (random.randint(1,sides))

def roll_6_and_8():
  roll_6 = diceRoll(6)
  roll_8 = diceRoll(8)
  health = roll_6 * roll_8
  return health

print("C H A R A C T E R ' S  H E A L T H S T A T")

character = "Y"

while character == "Y":
  ask_user = input("Name your character > ")
  health = str(roll_6_and_8())
  print("Their health is", "\033[33m",health,"\033[0m", "Hp.")

  character = input("Do you want to create an another character ( Y or N ) ? > ")
   
  

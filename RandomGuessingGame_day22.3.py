import random
print("...R A N D O M  N U M B E R  G U E S S I N G  G A M E...")
print()
attempts = 0
my_number = random.randint(1,100)

while True:
  print("Enter any number between 0 - 100.")
  input_number = int(input("> "))
  

  if my_number == input_number :
    print("You did it. The number was", my_number, ".")
    print("You took", attempts , "attempts to guess the number.")
    break

  attempts += 1
  
  if input_number <= 20:
    print("Too low.")
  elif input_number >= 20 and input_number <= 40:
    print("You're getting there!")
  elif input_number >= 40 and input_number <= 60:
    print("Somewhere in middle.")
  elif input_number > 60 and input_number <= 80:
    print("Little lower.")
  elif input_number >= 80 and input_number <= 100:
    print("Too high.")
  else:
    print("""Invalid input😡. Read the instruction properly.""")
     
  
  




    

print("...N U M B E R  L I S T  G E N E R A T O R...")
print()
print("You are going to give me a number you want  to start with, an ending number, and by how many you want me to add each time.")

print()
first_number = int(input("Start at > "))
ending_number = int(input("End before > "))
increment = int(input("Increment between values > "))

for i in range (first_number, ending_number, increment):
  print(i)
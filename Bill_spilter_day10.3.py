print("...Bill Spliter...")
print("Welcome! Say no more to using calculator😉")

#Calculate total amount per person
mybill = float(input("Enter the bill amount: Rs."))
no_of_people = int(input("""How many people are spliting the bill: """))

# Display each person's share
total_per_person = mybill / no_of_people
total_per_person = round(total_per_person, 2)

print("You each own Rs.", total_per_person)

# Ask if the user wants to leave a tip
tip = input("Do you want to leave a tip? : ")
if tip == "Yes" or tip == "yes":
 
  # Get the tip amount
  tip_amount = int(input("How much do you wanna tip? :Rs. "))
   # Calculate the final total per person including the tip
  final_total = total_per_person + tip_amount
 
  # Display each person's share with tip
  print("Your part of share after the tip is Rs. ", final_total)

else:
  print("Be generous and leave a tip, if you may!😝")
  
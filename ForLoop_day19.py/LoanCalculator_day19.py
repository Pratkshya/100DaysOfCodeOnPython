print("...L O A N  C A L C U L A T O R...")
print()
print("It'll show how much money you'll owe till 10 years!")
lent_money = int(input("Enter the amount of money you've borrowed > Rs."))
per_annum = 0.05

for year in range (10):
  lent_money += (lent_money * per_annum)
  print("Year", year +1, "is" , round(lent_money,2))

  

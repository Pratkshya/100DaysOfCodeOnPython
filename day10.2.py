print("Bill Spliter")
mybill = float(input("Enter the bill amount: "))
no_of_people = int(input("How many people? "))
answer = mybill / no_of_people 
answer = round(answer, 2)
print("You each own, Rs.", answer)
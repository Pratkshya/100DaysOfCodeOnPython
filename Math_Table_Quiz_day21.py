print("""Are you a math genious?
Oh well, we'll find that out👀
You'll be asked for a multiplication table for the number of your choice which you've to be prepared for to answer!
Don't be nervous😜""")
print()
print("Name your multiplies:")
number = int(input("> "))
print()

counter = 0
for i in range(1, 11):
  correct_answer = i*number
  print(i, "x", number)
  answer = int(input("> "))
  if answer == correct_answer:
    print("You got it right!")
    counter += 1
  else:
    print("That's not correct🫢. It should have been", correct_answer)
if counter == 10:
  print("Wow! A perfect score! 🥳 You're now a certified genious.")
else:
  print("You got", counter, "out of 10 correct.")
  
  




  
 

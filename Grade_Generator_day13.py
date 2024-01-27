print("...Exam Grade Generator...")
print()
subject_name = input("Enter your subject --> ")
full_marks = int(input("Enter the total marks --> "))
scored_marks = float(input("Enter your score --> "))

percentage = scored_marks / full_marks * 100
percentage = round(percentage, 2)

print()

print ("You scored : ","\033[32m" , percentage,"\033[0m","%")

if (percentage >= 90 and percentage <= 100 ):
  print("You got", "\033[35m","A+", "\033[0m","grade! CONGRATULATIONS🥳")

elif (percentage >= 80 and percentage <= 89):
  print("You got" , "\033[34m","A", "\033[0m","grade!","Great work!")

elif (percentage >= 70 and percentage <= 79):
 print("You got" , "\033[36m","B", "\033[0m","grade!", "A little push and you could ace your papers!")

elif (percentage >= 60 and percentage <= 69):
 print("You got" , "\033[33m","C", "\033[0m","grade!"," Still more to go and achieve!")

elif (percentage >= 50 and percentage <= 59):
 print("You got" ,  "\033[34m","D", "\033[0m","grade!","You can do so much better!")

elif (percentage <= 50 and percentage >= 1):
 print("You got" ,  "\033[36m","U", "\033[0m","grade!","Pull all nighter twice a week!😉")
else :
  print("Next time it'll sure work out. Keep trying!")
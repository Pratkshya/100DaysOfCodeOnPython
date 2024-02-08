def login():
  print("...Notebook Login...")
  print()
  user_name = "Pratikshya Parajuli"
  user_password = "desktop123"
  while True:
   data_input = input("Enter your user name > ")
   data_input2 = input("Enter your user password > ")
   
   if data_input == user_name and data_input2 == user_password:
     print("Welcome to Notebook!")
     break
    
   
   else:
    print("Your information doesn't match!!")
    print()
    continue

login()
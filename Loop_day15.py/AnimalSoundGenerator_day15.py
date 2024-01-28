print("..Animal Sound..")
print()

exit = ""
while exit != "yes" :
  animal_sound = input("Which animal sound do you want to know? --> ")
  if animal_sound == "Cow" or animal_sound == "cow":
    print("Moo 🐮")
  elif animal_sound == "Dog" or animal_sound == "dog":
    print("Woof 🐶 ")
  elif animal_sound == "Cat" or animal_sound == "cat":
    print("Meow 😺 ")
  elif animal_sound == "Pig" or animal_sound == "pig":
   print("Oink 🐷 ")
  elif animal_sound == "Chicken" or animal_sound == "chicken":
   print("Cluck 🐔 ")
  elif animal_sound == "Duck" or animal_sound == "duck":
   print("Quack 🦆 ")
  elif animal_sound == "Lion" or animal_sound == "lion":
     print("Roar 🦁 ")
  elif animal_sound == "Mouse" or animal_sound == "mouse":
     print("Chirps 🐭 ")

  else:
    print("I couldn't identify the animal. Try again!")

  exit = input("Do you want to exit? --> ")
   
    
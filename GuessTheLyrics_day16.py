print("Fill in the blank lyrics!")
print()
print("(Type in the missing word of a song, and see if you are as cool as me or not😈)")
print()

attempts = 1
while True:
  print("Killing in the _____ of.")
  guess = input("> ")
  print()
  if guess == "name":
    print("Wow. You indeed are cool🫢.")
    print("You only took", attempts, "attempt(s).")
    break
  else:
    print("Wrong word. Try again😡")
    print()
    attempts += 1
    
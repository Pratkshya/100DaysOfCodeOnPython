print("...Pin Generator...")
def pinGenerator(numbers):
  import random
  pin = ""
  for i in range (numbers):
    pin += str(random.randint(0,9))
  return pin

MyPin = pinGenerator(5)
print(MyPin)
  
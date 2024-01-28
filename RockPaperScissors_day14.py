from getpass import getpass as input  #To hide the player's input

print ("...E P I C  🪨   ✂️   📄  B A T T L E...")
print("Select R, S or P for your move.")
print()

player1_move = input("Player 1 --> ")
player2_move = input("Player 2 --> ")
print()

if player1_move == "R":
  if player2_move == "R" :
    print("You both picked Rock! Draw!")
  elif player2_move == "S":
    print("Player1's Rock smashed Player2's Scissors into million pieces!😝")
  elif player2_move == "P"  :
    print("Player1's Rock dominated Player2's Paper🥲")
  else:
    print("Invalid Move Player2 !!! 😡")

elif player1_move == "S":
  if player2_move == "R":
    print("Player2's Rock rocked Player2's tiny scissors😂")
  elif player2_move == "S":
    print("You both picked Scissors! Are you both predictable or what😒")
  elif player2_move == "P":
    print("Player1's Scissors cut Player2's Paper brurtely🫣")
  else :
    print ("Invalid Move Player2 !!! 😡")

elif player1_move == "P":
  if player2_move == "R":
    print("Player2's Rock smothered Player1's Paper.🫣")
  elif player2_move == "S":
    print("Player1's Paper was cut mercilessly by Player2's Scissors🫢")
  elif player2_move == "P"  :
    print("You both picked Paper. Draw!😶")
  else :
    print ("Invalid Move Player2 !!! 😡")

else :
  print("Invalid Move Player1 !!! 😡")









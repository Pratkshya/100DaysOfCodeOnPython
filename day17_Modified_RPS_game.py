from getpass import getpass as input  # To hide the player's input

print("...E P I C  🪨   ✂️   📄  B A T T L E...")
round = 1
player1_score = 0
player2_score = 0

while True:
    print()
    print("Round ", round)
    print("Select R, S or P for your move.")
    print()
    print("Player1_score ", player1_score)
    print("Player2_score ", player2_score)
    print()

    player1_move = input("Player 1 --> ")
    player2_move = input("Player 2 --> ")
    print()
    round += 1

    if player1_move == "R":
        if player2_move == "R":
            print("You both picked Rock! Draw!")
        elif player2_move == "S":
            print("Player1's Rock smashed Player2's Scissors into a million pieces! 😝")
            player1_score += 1
        elif player2_move == "P":
            print("Player1's Rock dominated Player2's Paper🥲")
            player1_score += 1
        else:
            print("Invalid Move Player2 !!! 😡")

    elif player1_move == "S":
        if player2_move == "R":
            print("Player2's Rock rocked Player1's tiny scissors😂")
            player2_score += 1
        elif player2_move == "S":
            print("You both picked Scissors! Are you both predictable or what😒")
        elif player2_move == "P":
            print("Player1's Scissors cut Player2's Paper brutally🫣")
            player2_score += 1
        else:
            print("Invalid Move Player2 !!! 😡")

    elif player1_move == "P":
        if player2_move == "R":
            print("Player2's Rock smothered Player1's Paper.🫣")
            player2_score += 1
        elif player2_move == "S":
            print("Player1's Paper was cut mercilessly by Player2's Scissors🫢")
            player2_score += 1
        elif player2_move == "P":
            print("You both picked Paper. Draw!😶")
        else:
            print("Invalid Move Player2 !!! 😡")

    else:
        print("Invalid Move Player1 !!! 😡")

    if player1_score == 3 or player2_score == 3:
        if player1_score == 3:
            print()
            print("Player 1 is the Winner!")
        else:
            print()
            print("Player 2 is the Winner!")
        break

import random

def RollDice(sides_of_a_dice):
    dice_roll = random.randint(1, sides_of_a_dice)
    print("You rolled", dice_roll)

def play_game():
    print("...Infinite Dice...")
    print()
    print("🎲")
    print()

    while True:
        sides_of_a_dice = int(input("How many sides? > "))
        RollDice(sides_of_a_dice)
        
        ask_user = input("Do you still want to play (Y or N)? > ")
        if ask_user.upper() != "Y":
            break
        print()

play_game()

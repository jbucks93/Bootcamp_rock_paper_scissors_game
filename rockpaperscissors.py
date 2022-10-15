import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if choice >= 3 or choice < 0:
    print("INVALID RESPONSE")
else:
    game_images = [rock, paper, scissors]

    print(game_images[choice])

    compchoice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[compchoice])

    if choice >= 3 or choice < 0:
        print("INVALID RESPONSE, you lose")
    elif choice == 0 and compchoice == 1:
        print("You lose")
    elif choice == 1 and compchoice == 2:
        print("You lose")
    elif choice == 2 and compchoice == 0:
        print("You lose")
    elif choice == compchoice:
        print("Tie")
    else:
        print("You win!")
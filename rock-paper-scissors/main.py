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
import random

rps_list = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0,2)

print(rps_list[user])
print("Computer chose:")
print(rps_list[computer])

if user >= 3 or user < 0:
  print("You typed an invalid number")
elif user == computer:
    print("Draw")
elif computer == 2 and user == 0:
    print("You win")
elif user == 2 and computer == 0:
    print("You lose")
elif user > computer:
    print("you win")
elif computer > user:
    print("you lose")

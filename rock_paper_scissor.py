import random as r
rock = '''   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
_______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissor = '''
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

gamelist = [rock,paper,scissor]
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

choicenumber = int(choice)
gamelistlength = len(gamelist)-1
randomselection = r.randint(0,gamelistlength)

print(f"\n{gamelist[choicenumber]}")

print("\nComputer choice:")

print(f"\n{gamelist[randomselection]}")

if choicenumber==0:
    if randomselection == 0:
        print("Game drawn")
    elif randomselection == 1:
        print("You lose")
    else:
        print("You won")
    
elif choicenumber == 1:
    if randomselection == 0:
        print("You won")
    elif randomselection == 1:
        print("Game drawn")
    else: 
        print("You lose")
elif choicenumber == 2:
    if randomselection == 0:
        print("You lose")
    elif randomselection == 1:
        print("You won")
    else: 
        print("Game drawn")
else:
    print("Your choice is out of scope, please rerun the game")
    

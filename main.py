import random
def game(computer, you):
    if computer == 'St':
        if you=='P':
            print("You win the game")
        elif you=='Sc':
            print("Computer win the game")
            print("You lose the game try another chance")
        else:
            print("The game will tie")
    elif computer == 'P':
        if you=='Sc':
            print("You win the game")
        elif you=='St':
            print("Computer win the game")
            print("You lose the game try another chance")
        else:
            print("The game will tie")
    elif computer == 'Sc':
        if you=='St':
            print("You win the game")
        elif you=='P':
            print("Computer win the game")
            print("You lose the game try another chance")
        else:
            print("The game will tie")
        

randNo = random.randint(1, 3)

if randNo == 1:
    computer = 'St'
elif randNo == 2:
    computer = 'P'
elif randNo ==3:
    computer = 'Sc'
print("Computer Turn: Stone(St) Paper(P) Scissor(Sc)?")
you = input("Your Turn: Stone(St) Paper(P) Scissor(Sc)?")
game(computer, you)
print(f"Computer choose {computer}")
print(f"You choose {you}")


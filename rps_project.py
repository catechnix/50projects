import random
choices = ('r','p','s')  
computer_score = 0
player_score = 0

def computer_choice(): 
     return (random.choice(choices)) #choice method of random module

def player_choice():  #to get the correct choice
    global choices
    symbol = input ("Input rock, paper or scissor, r for rock, p for paper, s for scissor:   ").lower()
    if symbol not in choices:
        print("You didn't enter the correct choice. ")
        return player_choice() # use recursion to get a valid input
    else:
        return symbol

def rps_game():

    global cChoice, pChoice
    

    pChoice= player_choice()
    cChoice= computer_choice()
    print("The computer has chosen \n", cChoice)
    print("The player's choice \n", pChoice)

    if cChoice == pChoice:
        print ("It is a tie, no one gets a point")
    elif (pChoice == "r" and cChoice == "s") or (pChoice == 's' and cChoice == 'p') or (pChoice == 'p' and cChoice == 'r' ):
        print("The player won!")
        player_score += 1 #increment the players point by 1
     
    else:
        print("Computer won!")
        computer_score +=1
    print()

    
def main():
    print("Welcome to the Rock, paper and Scissor's game!!!")
    print("\n")

    while True:
        for i in range(5):
            rps_game()

        print ("Player score {0} and computer score {1} are".format(player_score, computer_score))
        print() # print an empty line

    print("Do you want to continue? Enter 1; do you want to reset and continue, enter 2, do you want to quit, enter 3")

    wish_number =int(input())
    if wish_number == 1:
        continue
    elif wish_number == 2:
        player_score = 0
        computer_score =0
        continue
    else wish_number == 3:
        break

print ("OK, Bye!")

if __name__ == '__main__':
    main()


    

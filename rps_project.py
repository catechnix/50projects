import random
rps = ()
computer_score = 0
player_score = 0

def user_input_for_game():
    user_input = input ("Input rock, paper or scissor, r for rock, p for paper, s for scissor")
    if user_input in (rps):
        return user_input
    else:
        user_input_for_game()

def computer_choice(): 
     return (random())

def rps_game():
    x=user_input_for_game()
    y=computer_choice()
    if x == y:
        print ("It is a tie, no one gets a point")
    elif x == "r" and y == "s":
        player_score += 1
    
    elif x == "s" and y == "p":
        player_score +=1
    
    elif x == "p " and y == "r":
        player_score += 1
    
    else:
        computer_score +=1

    print ("Player score {0} and computer score {1} are".format(player_score, computer_score))


def main():
    print("Welcome to the Rock, paper and Scissor's game\n")
    
    for in range(4):
        rps_game()

    print("Do you want to continue? Enter 1; do you want to reset and continue, enter 2, do you want to quit, enter 3")

    wish_number =input()
    if wish_number == '1':
        rps_game()
    elif wish_number == '2':
        player_score = 0
        computer_score =0
        for in range(4):
        rps_game()
    elif wish_number == "3":
        exit()

if __name__ == __main__
    main()


    

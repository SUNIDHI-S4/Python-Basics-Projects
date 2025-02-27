import random 

def play() :
    user = input("Enter 'r' for rock, 'p' for paper and 's' for scissors \nWhat's your choice : " ).lower()
    computer = random.choice(['r','p','s'])

    if user == computer : 
        return "It's a Tie"

    if is_win(user,computer) :
        return "You Won !"
    return "Computer Won !"

def is_win(player,opponent) :
    #returns true if player wins
    # r>s, s>p, p>r
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r':
        return True 

print(play())
import sys

player1 = input("Entre your name ")
player2 = input("Entre your name")
choose1 = input("%s, what to want to choose rock, paper or scissors?" % player1)
choose2 = input("%s, what to you want to choose rock, paper or scissors?" % player2)

def compare(p1, p2):
    if p1 == p2:
        return("It's a tie!")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif p1 == 'scissors':
        if p2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif p1 == 'paper':
        if p2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(choose1, choose2))
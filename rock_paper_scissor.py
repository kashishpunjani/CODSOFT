#.................................... rock paper scissor game ......................................


import random
print('Rock beats scissors, scissors beat paper, and paper beats rock, win score  = 2, loose score  = 0, tie score = 1')
while True:
    user = input("enter the choice (rock,paper,scissor): ")
    rand = ('rock' ,'paper','scissor')
    computer = random.choice(rand)
    print('computer choice is : ',computer)

    user_win = 0
    computer_win = 0

    if user == computer :
        print('its tie')
        print('score---->')
        user_win+=1
        computer_win+=1
        print("it's tie user score = ",user_win)
        print("it's tie computer score = ",user_win)

    elif user == 'rock' :
        if computer == 'scissor':
            print('user win')
            print('score---->')
            user_win+=2
            print('user score = ',user_win)
            print('computer score = ',computer_win)
        else:
            print('computer win')
            print('score---->')
            computer_win+=2
            print('user score = ',user_win)
            print('computer score = ',computer_win)


    elif user == 'paper' :
        if computer == 'rock':
            print('user win')
            print('score---->')
            user_win+=2
            print('user score = ',user_win)
            print('computer score = ',computer_win)
        else:
            print('computer win')
            print('score---->')
            computer_win+=2
            print('user score = ',user_win)
            print('computer score = ',computer_win)

    elif user == 'scissor' :
        if computer == 'paper':
            print('user win')
            print('score---->')
            user_win+=2
            print('user score = ',user_win)
            print('computer score = ',computer_win)
        else:
            print('computer win')
            print('score---->')
            computer_win+=2
            print('user score = ',user_win)
            print('computer score = ',computer_win)



    else:
        print('enter valid choice')



    game = input('want to play again? (y/n)  : ')
    if game.lower() == 'n':
        break

feedback = input('want to give feedback? (yes/no)  : ')
if feedback == 'yes':
    x = input('Please enter your feedback!')
else:
    print('')


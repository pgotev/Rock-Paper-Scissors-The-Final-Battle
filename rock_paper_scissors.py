import random
# First we make sure the player wants to start playing or not
print('Are you ready for the most exiting game of Rock, Paper, Scissors ever?')
ready_or_not = input('Type in your answer here. [Y]es or [N]o? ').lower()
mistake_counter = 0

while True:
    if ready_or_not == 'y' or ready_or_not == 'yes':
        print('OK. Lets begin!')
        print('------------------------------------------')
        break
    elif ready_or_not == 'n' or ready_or_not == 'no':
        print('OK, but you\'re missing out. Goodbye.')
        exit()
    else:
        if mistake_counter == 0:
            print('This is an invalid command. I hope this was an honest mistake and you\'re not trying to test my'
                  ' patience. Just type Y to start playing or N to exit the program: ', end='')
            mistake_counter += 1
            ready_or_not = input().lower()
        elif mistake_counter == 1:
            print('This is your second invalid command. If you want to play you have to follow my commands. Type in Y to start or N to exit: ', end='')
            mistake_counter += 1
            ready_or_not = input().lower()
        elif mistake_counter == 2:
            print('This is your third invalid command. You get one more chance but after that it\'s over. I mean it. ', end='')
            mistake_counter += 1
            ready_or_not = input().lower()
        elif mistake_counter > 2:
            print('I wasn\'t bluffing. END GAME')
            exit()

print('To pick just type in the first letter of your choice:')
print('[R]: Rock')
print('[P]: Paper')
print('[S]: Scissors')
print()
print('For detailed explanation of the rules of the game type in: Help')

players_choice_input = input('What will it be: ').lower()
print('------------------------------------------')

if players_choice_input == 'help' or players_choice_input == 'h':
    print('You dont know the rules of Rock, Paper, Scissors? Really? OK, here you go: Rock beats scissors, scissors beat paper and paper beats rock.')
    players_choice_input = input('Now that you know all about the game, make your pick already: Rock, Paper or Scissors? ').lower()

mistake_counter = 0
while True:
    if players_choice_input == 'r':
        players_choice = 'Rock'
        break
    elif players_choice_input == 'p':
        players_choice = 'Paper'
        break
    elif players_choice_input == 's':
        players_choice = 'Scissors'
        break
    else:
        if mistake_counter == 0:
            print('Invalid command. You have one more chance:')
            mistake_counter += 1
            players_choice_input = input('Type in R for Rock, P for Paper or S for Scissors: ')
        else:
            print('Invalid command.')
            raise SystemExit()

print(f'You have chosen: {players_choice} This is a wise choice. It\'s proven to be one of the Top 3 best choices you '
      f'can make. You\'re clearly good at this game, but let\'s see what your mighty opponent has prepared for you.')

computer_random_move = random.randint(1, 3)
computer_choice = ''
if computer_random_move == 1:
    computer_choice = 'Rock'
elif computer_random_move == 2:
    computer_choice = 'Paper'
elif computer_random_move == 3:
    computer_choice = 'Scissors'

print(f'The computer picks: {computer_choice}')

match_result = ''
if players_choice == computer_choice:
    match_result = 'Draw'
elif (players_choice == 'Rock' and computer_choice == 'Scissors' or
      players_choice == 'Paper' and computer_choice == 'Rock' or
      players_choice == 'Scissors' and computer_choice == 'Paper'):
    match_result = 'Player wins'
elif (players_choice == 'Rock' and computer_choice == 'Paper' or
      players_choice == 'Paper' and computer_choice == 'Scissors' or
      players_choice == 'Scissors' and computer_choice == 'Rock'):
    match_result = 'Computer wins'

print(match_result)



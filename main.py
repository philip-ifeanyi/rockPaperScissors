from random import choice

moves = ['R', 'P', 'S']
user_move = input('Choose a move, "R" for Rock, "P" for Paper, "S" for Scissors: ').upper()
CPU_move = choice(moves)
game_on = True


while game_on:
  if user_move in moves: 
    print('Your move ({}) : CPU Move ({})'.format(user_move, CPU_move))
    if user_move == 'R':
      if CPU_move == 'R':
        user_move = input('It is a tie, choose a move, "R" for Rock, "P" for Paper, "S" for Scissors: ').upper()
        CPU_move = choice(moves)
      elif CPU_move == 'P':
        print("Paper covers Rock, You Lose!")
        game_on = False
      elif CPU_move == 'S':
        print("Rock breaks Scissors, You Win!")
        game_on = False
    elif user_move == 'P':
      if CPU_move == 'P':
        user_move = input('It is a tie, choose a move, "R" for Rock, "P" for Paper, "S" for Scissors: ').upper()
        CPU_move = choice(moves)
      elif CPU_move == 'R':
        print("Paper covers Rock, You Win!")
        game_on = False
      elif CPU_move == 'S':
        print("Scissors cuts Paper, You Lose!")
        game_on = False
    elif user_move == 'S':
      if CPU_move == 'S':
        user_move = input('It is a tie, choose a move, "R" for Rock, "P" for Paper, "S" for Scissors: ').upper()
        CPU_move = choice(moves)
      elif CPU_move == 'P':
        print("Scissors cuts Paper, You Win!")
        game_on = False
      elif CPU_move == 'R':
        print("Rock breaks Scissors, You Lose!")
        game_on = False
  else:
    user_move = input('Invalid Move!, Pick "R" for Rock, "P" for Paper, "S" for Scissors: ').upper()
    continue
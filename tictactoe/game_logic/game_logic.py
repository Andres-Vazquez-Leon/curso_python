"""
Docstring for tictactoe.game_logic.game_logic
Author: Andrés Manuel Vazquez León
Here goes the logic for Tictactoe
"""
import board #trae el board del mismo direct
import random

def check_winner(d:dict, combo_list:list)->bool:
    """chech if there is a winner"""
    for combo in combo_list:
        if d[combo[0]] == d[combo[1]] == d[combo[2]]:
            return True
    return False

def game(num_players:int)->str:
    """
    Here lives the main game loop
    """
    turns = 0
    dboard = {x:str(x) for x in range(9)}
    combo_list = [
        [0,1,2],  [3,4,5],  [6,7,8], #Rows
        [0,3,6],  [1,4,7],  [2,5,8], #Columns
        [0,4,8],  [2,4,6]            #Diagonals
    ]
    x_player = 'X'
    O_player = 'O'
    current_player = x_player
    winner = False
    w_player = ""
    while turns < 9 and not winner: # ejecuta el coidgo mientra sea menor a 9
        board.display_board(dboard)
        #valid_move = False
        
        if num_players == 1:
            one_player(current_player, dboard)

        else:
            if num_players == 2:
                two_player(current_player, dboard)

        turns += 1 
        winner = check_winner(dboard, combo_list)
        if winner:
            w_player = current_player
        if current_player == x_player:
            current_player = O_player
        else: current_player = x_player
    board.display_board(dboard)
    return w_player

def play_game(players = 2)->None:
    """
    Two Players game loop
    """
    playing = True
    score = {'X':0, 'O':0, 'Ties':0}
    while playing:
        winner = game(players)
        if len(winner) > 0:
            print(f"Winner: Player {winner}")
        else:
            print("It's A tie")
            winner = 'Ties'
        score[winner] += 1
        replay = input("do you want to play again (y/n): ").strip().lower
        if replay != 'y':
            playing = False
    print(f"Score: X = {score['X']}, O = {score['O']}, Ties = {score['Ties']}")
    #if winner:
    #    print(f"winner: Player {w_player}")
    #else:
    #    print("It's a tie")


def one_player(current_player:str, dboard:dict)->None:
    valid_move = False
    x_player = 'X'
    o_player = 'O'
    if current_player == x_player:
        while not valid_move:
            valid_move = board.player_turn(current_player, dboard)
    else:
        print("Computer's turn:")
        while not valid_move:
            move = random.randint(0,8)
            if str(dboard[move]) == str(move):
                dboard[move] = o_player
                valid_move = True

def two_player (current_player:str, dboard:dict):
    """
    Two player game loop
    """
    valid_move = False
    while not valid_move:
        valid_move = board.player_turn(current_player, dboard)


if __name__ == "__main__":
    play_game(1)
    
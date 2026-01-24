"""
Docstring for tictactoe.game_logic.game_logic
Author: Andrés Manuel Vazquez León
Here goes the logic for Tictactoe
"""
import board #trae el board del mismo directorio
def check_winner(d:dict, combo_list:list)->bool:
    """chech if there is a winner"""
    for combo in combo_list:
        if d[combo[0]] == d[combo[1]] == d[combo[2]]:
            return True
    return False

def game():
    """
    Here lives the main game loop
    """
    turns = 0
    dboard = {x:str(x) for x in range(9)}
    combo_list = [
        [0,1,2],  [3,4,5],  [6,7,8],
        [0,3,6],  [1,4,7],  [2,5,8],
        [0,4,8],  [2,4,6]
    ]
    x_player = 'X'
    O_player = 'O'
    current_player = x_player
    while turns < 9: # ejecuta el coidgo mientra sea menor a 9
        board.display_board(dboard)
        valid_move = False
        while not valid_move:
            valid_move = board.player_turn (current_player, dboard)
        turns += 1 
        if current_player == x_player:
            current_player = O_player
        else: current_player = x_player

if __name__ == "__main__":
    game()
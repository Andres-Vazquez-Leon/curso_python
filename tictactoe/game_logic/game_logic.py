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

def game()->str:
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
    winner = False
    w_player = ""
    while turns < 9 and not winner: # ejecuta el coidgo mientra sea menor a 9
        board.display_board(dboard)
        valid_move = False
        while not valid_move:
            valid_move = board.player_turn (current_player, dboard)
            #check_winner(dboard, combo_list)

            """if check_winner(dboard, combo_list) == True:
                print("ganaste")
                turns = 8
                board.display_board(dboard)"""

        turns += 1 
        winner = check_winner(dboard, combo_list)
        if winner:
            w_player = current_player
            print(f"Player {current_player} wins!")
        if current_player == x_player:
            current_player = O_player
        else: current_player = x_player
    board.display_board(dboard)
    return w_player
    #if winner:
    #    print(f"winner: Player {w_player}")
    #else:
    #    print("It's a tie")




if __name__ == "__main__":
   win = game()
   if win:
       print (f"Winner: player {win}")
   else:
       print("Is's a tie")
    
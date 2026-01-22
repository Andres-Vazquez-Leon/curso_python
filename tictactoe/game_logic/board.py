'''Andres Manuel Vazquez Leon
'''
def display_board(dboard:dict)->None:
   """Display board game based of toctactoe"""
   d = display_board
   print(f"{d[0]:2s}|{d[1]:2s}|{d[2]:2s}")
   print("---+---+---+")
   print(f"{d[3]:2s}|{d[4]:2s}|{d[5]:2s}")
   print("---+---+---+")
   print(f"{d[6]:2s}|{d[7]:2s}|{d[8]:2s}")
   print("---+---+---+")

def player_turn(payer:str, dboard:dict)->int:
   """Ask player for their turn"""

if __name__ == "__main__":
   board = {x:str(x) for x in range(9)}
   display_board(board)
   board[0] = 'X'
   board[4] = '0'
   display_board(board)
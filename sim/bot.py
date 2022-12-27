import random

class TicTacToeBot:
    def __init__(self):
        self.remaining_moves = None
        self.bot_symbol = None
    
    def update_bot_symbol(self, bot_symbol):
        self.bot_symbol = bot_symbol
        self.remaining_moves = 5 if bot_symbol == 'O' else 4

    def get_move(self, board):
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board[row][col] == '-':
                self.remaining_moves -= 1  
                return row + 1, col + 1

              

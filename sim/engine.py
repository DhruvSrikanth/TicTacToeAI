import random

class TicTacToe:
    def __init__(self):
        self.board = self.create_board()
        
    def create_board(self):
        board = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append('-')
            board.append(row)
        return board

    def determine_p1(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player_symbol):
        self.board[row][col] = player_symbol

    def is_player_win(self, player_symbol):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player_symbol:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player_symbol:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player_symbol:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player_symbol:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player_symbol):
        return 'X' if player_symbol == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self, bot):
        player_symbol = 'O'
        bot_move = bool(self.determine_p1())
        bot.update_bot_symbol(player_symbol if bot_move else self.swap_player_turn(player_symbol))

        while True:
            print("-" * 25)
            print("Board:")
            self.show_board()

            if bot_move:
                # bot's turn
                row, col = bot.get_move(self.board)
                print(f"T played {player_symbol} at {row}, {col}.")
            else:
                # your turn
                # taking user input
                row, col = list(
                    map(int, input("Enter row and column: ").split())
                )
                print()
            print("-" * 25)
            
            # fixing the spot
            self.fix_spot(row - 1, col - 1, player_symbol)

            # checking whether current player is won or not
            if self.is_player_win(player_symbol):
                print("-" * 25)
                if bot_move:
                    print(f"Bot {player_symbol} won!")
                else:
                    print(f"You {player_symbol} won!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("-" * 25)
                print("Draw!")
                break

            # swapping the turn
            player_symbol = self.swap_player_turn(player_symbol)
            bot_move = not bot_move

        # showing the final view of board
        print("Final Board:")
        self.show_board()
        print("-" * 25)


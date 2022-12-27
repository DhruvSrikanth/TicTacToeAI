from .engine import TicTacToe
from .bot import TicTacToeBot

if __name__ == '__main__':
    # creating a new game
    game = TicTacToe()

    # creating a new bot
    bot = TicTacToeBot()

    # starting the game
    game.start(bot=bot)


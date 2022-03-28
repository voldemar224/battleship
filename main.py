from battleship import Battleship
from tk_modified import TkModified


main_window = TkModified()

game = Battleship(main_window)

game.start()

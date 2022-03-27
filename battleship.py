import tkinter as tk
from tk_modified import TkModified


class Battleship:
    def __init__(self):
        pass

    def start(self):
        self.create_fields()
        #  main loop

        # while not self.game_over():
        #     self.make_move()
        # else:
        #     self.open_fields()

    def create_fields(self):
        main_window = TkModified()
        main_window.mainloop()

    def make_move(self):
        if self.left_player.turn:
            self.left_player.move()
            self.left_player.turn = False
            self.right_player.turn = True
        else:
            self.right_player.move()
            self.right_player.turn = False
            self.left_player.turn = True

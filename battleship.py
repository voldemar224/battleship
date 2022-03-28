import tkinter as tk
from tk_modified import TkModified

from const import player_field_height as pfh
from const import player_field_width as pfw


class Battleship:
    def __init__(self, window=None, left_field_table=None, right_field_table=None):

        self.window = window

        if left_field_table is None:
            self.left_field_table = []

        if right_field_table is None:
            self.right_field_table = []

        # filling tables with 0s
        for row in range(pfh):
            self.left_field_table.append([])
            for col in range(pfw):
                self.left_field_table[row].append(0)

        for row in range(pfh):
            self.right_field_table.append([])
            for col in range(pfw):
                self.right_field_table[row].append(0)

    def start(self):
        self.create_fields()

        #  main loop

        # while not self.game_over():
        #     self.make_move()
        # else:
        #     self.open_fields()

    def create_fields(self):

        self.window.readiness_button.configure(command=self.setting_ships)

        self.window.draw_game()

        self.window.mainloop()

    def setting_ships(self):

        for ship in self.window.left_field_ships:
            self.left_field_table[ship[1]][ship[0]] = 1

        for ship in self.window.right_field_ships:
            self.right_field_table[ship[1]][ship[0]] = 1

        for row1 in self.left_field_table:
            print(row1)

        for row2 in self.right_field_table:
            print(row2)

    def make_move(self):
        if self.left_player.turn:
            self.left_player.move()
            self.left_player.turn = False
            self.right_player.turn = True
        else:
            self.right_player.move()
            self.right_player.turn = False
            self.left_player.turn = True

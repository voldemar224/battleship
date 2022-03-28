import tkinter as tk
import random

from const import player_field_height as pfh
from const import player_field_width as pfw

from const import upper_field_shift as ufs

from const import left_field_shift as lf_fs

from const import between_fields as bw

from const import field_height as fh
from const import field_width as fw

from const import cell_size_pxl as csp
from const import button_size_pxl as bsp

from const import letters

from const import font, font_size

from const import readiness_button_x as rbx
from const import readiness_button_y as rby
from const import readiness_button_width as rbw

from button_modified_player import ButtonModifiedPlayer
from button_modified_enemy import ButtonModifiedEnemy


class TkModified(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk',
                 useTk=True, sync=False, use=None,
                 height=fh, width=fw, left_field_ships=None, right_field_ships=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        if left_field_ships is None:
            self.left_field_ships = []
        if right_field_ships is None:
            self.right_field_ships = []

        self.height = height
        self.width = width
        self.readiness_button = tk.Button(self, width=4, height=2, bd=1, relief='solid', bg='grey')

    def draw_game(self):
        pixel = tk.PhotoImage(width=1, height=1)
        #  num of letter, which we draw
        letter_num = 0
        #  num, which we draw
        num = 1

        for row in range(self.height):
            for col in range(self.width):

                # temporary readiness_button
                if row == rby and col in range(rbx[0], rbx[1]):

                    self.readiness_button.grid(row=row, column=col)

                # checking if the place is for frame
                elif not (row in range(ufs, ufs + pfh) and
                          (col in range(lf_fs, lf_fs + pfw)
                           or col in range(lf_fs + pfw + bw, lf_fs + pfw + bw + pfw))):

                    # creating background cells
                    frame = tk.Frame(width=csp, height=csp, relief='solid', bd=1, bg='white')

                    # checking if we have to add letter in this frame
                    if (col == lf_fs - 1 or col == lf_fs + pfw + bw - 1) and (row in range(ufs, ufs + pfh)):

                        num_label = tk.Label(frame, text=str(int(num)), bg='white', font=font + " " + font_size)

                        num_label.place(x=csp / 2, y=csp / 2, anchor=tk.CENTER)

                        num += 0.5

                    # checking if we have to add number in this frame
                    elif (row == ufs - 1) and (col in range(lf_fs, lf_fs + pfw) or
                                               col in range(lf_fs + pfw + bw, lf_fs + pfw + bw + pfw)):

                        letter = tk.Label(frame, text=letters[letter_num], bg='white', font=font + " " + font_size)

                        letter.place(x=csp / 2, y=csp / 2, anchor=tk.CENTER)

                        letter_num = (letter_num + 1) % pfw

                    frame.grid(row=row, column=col)
                # buttons
                else:
                    # left_field buttons
                    if col in range(lf_fs, lf_fs + pfw):
                        button = ButtonModifiedPlayer(x=col - lf_fs, y=row - ufs, image=pixel, width=bsp, height=bsp,
                                                      bd=1, relief='solid', bg='cyan')

                        button.grid(row=row, column=col)
                    # right_field buttons
                    elif col in range(lf_fs + pfw + bw, lf_fs + pfw + bw + pfw):
                        button = ButtonModifiedEnemy(x=col - lf_fs - pfw - bw, y=row - ufs, image=pixel, width=bsp, height=bsp,
                                                     bd=1, relief='solid', bg='red')

                        button.grid(row=row, column=col)

        self.mainloop()

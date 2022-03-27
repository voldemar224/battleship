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


class TkModified(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk',
                 useTk=True, sync=False, use=None, height=fh, width=fw):
        super().__init__(screenName, baseName, className,
                         useTk, sync, use)
        self.height = height
        self.width = width

        self.fill_with_buttons()

    def fill_with_buttons(self):
        pixel = tk.PhotoImage(width=1, height=1)

        for row in range(self.height):
            for col in range(self.width):
                if not (row in range(ufs, ufs + pfh) and
                        (col in range(lf_fs, lf_fs + pfw)
                         or col in range(lf_fs + pfw + bw, lf_fs + pfw + bw + pfw))):
                    tk.Frame(width=csp, height=csp, relief='solid', bd=1, bg='white').grid(row=row, column=col)
                else:
                    tk.Button(image=pixel, width=bsp, height=bsp,
                              bd=1, relief='solid', bg='cyan').grid(row=row, column=col)

        self.mainloop()

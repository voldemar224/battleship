import tkinter as tk


class ButtonModifiedPlayer(tk.Button):
    def __init__(self, x, y, master=None, cnf={}, **kw):
        super().__init__(master=None, cnf={}, **kw)
        self.x = x
        self.y = y

        self.configure(command=self.left_click)
        self.bind('<Button-3>', self.right_click)

    def left_click(self):
        self.configure(bg='green')
        self.master.left_field_ships.append((self.x, self.y))
        print("left_field_ships", self.master.left_field_ships)
        print("right_field_ships", self.master.right_field_ships)
        print()

    def right_click(self, argument):
        self.configure(bg='cyan')
        if (self.x, self.y) in self.master.left_field_ships:
            self.master.left_field_ships.remove((self.x, self.y))
            print("left_field_ships", self.master.left_field_ships)
            print("right_field_ships", self.master.right_field_ships)
            print()


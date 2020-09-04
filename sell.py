from tkinter import *


class One:
    def __init__(self, sell_win):
        self.sell_win = sell_win
        self.sell_win.geometry('1920x1080')
        self.sell_win.config(bg='#ffffff')


def main():
    sell_win = Tk()
    One(sell_win)
    sell_win.mainloop()


if __name__ == "__main__":
    main()

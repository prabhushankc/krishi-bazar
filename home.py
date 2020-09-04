from tkinter import *
import sell
import buy


class Base:
    def __init__(self, gg):
        self.gg = gg
        self.gg.geometry('1920x1080')
        self.gg.config(bg='#ffffff')

        self.frame1 = LabelFrame(gg, text='Krishi Bazar', font=('arial', 12, 'bold'), padx=5, pady=5, fg='green',
                                 bg='#ffffff')
        self.frame1.pack()

        self.title = Label(self.frame1, text='What are you here for?', font=('arial', 24, 'bold'), fg="green",
                           bg='#ffffff')
        self.title.grid(row=0, column=1)

        self.sell = Button(self.frame1, text='Sell', font=('arial', 20, 'bold'), fg='#ffffff', bg='green',
                           activebackground='#ffffff', activeforeground='green', width=20, pady=40,
                           command=self.open_sell)
        self.sell.grid(row=1, column=1)

        self.buy = Button(self.frame1, text='Buy', font=('arial', 20, 'bold'), fg='#ffffff', bg='green',
                          activebackground='#ffffff', activeforeground='green', width=20, pady=40)
        self.buy.grid(row=2, column=1)

    def open_sell(self):
        self.gg.withdraw()
        win = Toplevel(self.gg)
        sell.One(win)

    def open_buy(self):
        self.gg.withdraw()
        buy_win = Toplevel(self.gg)
        buy.Two(buy_win)


def main():
    gg = Tk()
    Base(gg)
    gg.mainloop()


if __name__ == "__main__":
    main()

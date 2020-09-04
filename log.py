from tkinter import *
import Reg
from tkinter import messagebox
from connect import Dbase
import buy


class LogIn:
    def __init__(self, log):

        self.dat = Dbase()
        self.log = log
        self.log.geometry('1920x1080')
        self.log.config(bg='#ffffff')

        self.frame = LabelFrame(log, text='Krishi Bazar', font=('arial', 12, 'bold'), padx=5, pady=5, fg='green',
                                bg='#ffffff')
        self.frame.pack()

        self.title = Label(self.frame, text='Log In', font=('arial', 24, 'bold'), fg="green", bg='#ffffff')
        self.title.grid(row=0, column=1)

        self.lb_id = Label(self.frame, text='User Name', font=('arial', 20, 'bold'), fg='green', bg='white')
        self.lb_id.grid(row=1, column=1)

        self.en_id = Entry(self.frame, font=('arial', 20), width=20, fg='green')
        self.en_id.grid(row=2, column=1)

        self.lb_psw = Label(self.frame, text='Password', font=('arial', 20, 'bold'), fg='green', bg='white')
        self.lb_psw.grid(row=3, column=1)

        self.en_psw = Entry(self.frame, font=('arial', 20), width=20, show='*', fg='green')
        self.en_psw.grid(row=4, column=1)

        self.log_btn = Button(self.frame, font=('arial', 20), text="LogIn", bg="green", fg='white',
                              activeforeground='green', activebackground='white', width=11, command=lambda: self.logbtn(self.en_id.get(), self.en_psw.get()))
        self.log_btn.grid(row=5, column=1, sticky="E")

        self.res_btn = Button(self.frame, font=('arial', 20), text='Reset', bg='green',
                              fg='white', activeforeground='green', activebackground='white', command=self.reset,
                              width=10)
        self.res_btn.grid(row=5, column=1, sticky="W")

        self.f2 = LabelFrame(self.frame, text='Do not have an account?', font=('arial', 20, 'bold'), padx=5, pady=5,
                             fg='green', bg='#ffffff')
        self.f2.grid(row=6, column=1)
        self.btn_reg = Button(self.f2, font=('arial', 20, 'bold'), text="Register", bg="green", fg='white',
                              activeforeground='green', activebackground='white', command=self.register)
        self.btn_reg.pack()

    def logbtn(self, a, b):

        if a == '' or b == '':
            messagebox.showerror('error', 'Please fill all the data')

        else:
            firta = self.dat.forlogin(a, b)
            if len(firta) > 0:
                messagebox.showinfo('sucess', 'sucessfully logged in')
                self.log.withdraw()
                win = Toplevel(self.log)
                buy.Two(win)
                return True
            else:
                messagebox.showerror('error', 'invalid password or username')
                return False

    def register(self):
        self.log.withdraw()
        nw = Toplevel(self.log)
        Reg.Reg(nw)

    def reset(self):
        self.en_id.delete(0, END)
        self.en_psw.delete(0, END)


def main():
    log = Tk()
    LogIn(log)
    log.mainloop()


if __name__ == "__main__":
    main()

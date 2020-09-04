from tkinter import *
from connect import Dbase
from tkinter import messagebox
import log


class Reg:
    def __init__(self, log):
        self.nam = Dbase()

        self.log = log
        self.log.geometry('1920x1080')
        self.log.config(bg='#ffffff')

        self.frame = LabelFrame(log, text='Krishi Bazar', font=('arial', 12, 'bold'), padx=5, pady=5, fg='green',
                                bg='#ffffff')
        self.frame.pack()

        self.title = Label(self.frame, text='Register', font=('arial', 24, 'bold'), fg="green", bg='#ffffff')
        self.title.grid(row=0, column=1, columnspan=2)

        self.name_lb = Label(self.frame, text='Name', font=('arial', 20, 'bold'), fg='green', bg='#FFFFFF')
        self.name_lb.grid(row=1, column=1)
        self.name_en = Entry(self.frame, font=('arial', 20), fg='green', bg='#ffffff', width=15)
        self.name_en.grid(row=1, column=2)

        self.psw_lb = Label(self.frame, text='Password', font=('arial', 20, 'bold'), fg='green', bg='#FFFFFF')
        self.psw_lb.grid(row=2, column=1)
        self.psw_en = Entry(self.frame, font=('arial', 20), fg='green', bg='#ffffff', width=15, show='*')
        self.psw_en.grid(row=2, column=2)

        self.con_psw_lb = Label(self.frame, text='Confirm Password', font=('arial', 20, 'bold'), fg='green',
                                bg='#FFFFFF')
        self.con_psw_lb.grid(row=3, column=1)
        self.con_psw_en = Entry(self.frame, font=('arial', 20), fg='green', bg='#ffffff', width=15, show='*')
        self.con_psw_en.grid(row=3, column=2)

        self.uname_lb = Label(self.frame, text='User Name', font=('arial', 20, 'bold'), fg='green', bg='#FFFFFF')
        self.uname_lb.grid(row=4, column=1)
        self.uname_en = Entry(self.frame, font=('arial', 20), fg='green', bg='#ffffff', width=15)
        self.uname_en.grid(row=4, column=2)

        self.dob_lb = Label(self.frame, text='D.O.B.', font=('arial', 20, 'bold'), fg='green', bg='#FFFFFF')
        self.dob_lb.grid(row=5, column=1)
        self.dob_en = Entry(self.frame, font=('arial', 20), fg='green', bg='#ffffff', width=15, text='yy/mm/dd')
        self.dob_en.grid(row=5, column=2)

        self.gender_lb = Label(self.frame, text='Gender', font=('arial', 20, 'bold'), fg='green', bg='#FFFFFF')
        self.gender_lb.grid(row=6, column=1)
        self.gender_en = Entry(self.frame, font=('arial', 20), fg='green', bg='#ffffff', width=15)
        self.gender_en.grid(row=6, column=2)

        self.address_lb = Label(self.frame, text='Address', font=('arial', 20, 'bold'), fg='green', bg='#FFFFFF')
        self.address_lb.grid(row=7, column=1)
        self.address_en = Entry(self.frame, font=('arial', 20), fg='green', bg='#ffffff', width=15)
        self.address_en.grid(row=7, column=2)

        self.phone_lb = Label(self.frame, text='Phone no.', font=('arial', 20, 'bold'), fg='green', bg='#FFFFFF')
        self.phone_lb.grid(row=8, column=1)
        self.phone_en = Entry(self.frame, font=('arial', 20), fg='green', bg='#ffffff', width=15)
        self.phone_en.grid(row=8, column=2)

        self.mail_lb = Label(self.frame, text='E-Mail', font=('arial', 20, 'bold'), fg='green', bg='#FFFFFF')
        self.mail_lb.grid(row=9, column=1)
        self.mail_en = Entry(self.frame, font=('arial', 20), fg='green', bg='#ffffff', width=15)
        self.mail_en.grid(row=9, column=2)

        self.reg_btn = Button(self.frame, text='Register', font=('arial', 20, 'bold'), fg='#ffffff', bg='green',
                              width=15, activeforeground='green', command=self.save)
        self.reg_btn.grid(row=10, column=2, sticky='W')

        self.res_btn = Button(self.frame, text='Reset', font=('arial', 20, 'bold'), fg='#ffffff', bg='green', width=15,
                              activeforeground='green', command=self.resbtn)
        self.res_btn.grid(row=10, column=1, sticky='E')

        self.return_btn = Button(self.frame, text='Home', font=('arial', 20, 'bold'), fg='#ffffff', bg='green', width=15,
                                 activeforeground='green', command=self.back)
        self.return_btn.grid(row=11, column=1, columnspan=4)

    def back(self):
        self.log.withdraw()
        nw = Toplevel(self.log)
        log.LogIn(nw)

    def resbtn(self):
        self.name_en.delete(0, END)
        self.psw_en.delete(0, END)
        self.uname_en.delete(0, END)
        self.mail_en.delete(0, END)
        self.gender_en.delete(0, END)
        self.phone_en.delete(0, END)
        self.con_psw_en.delete(0, END)
        self.gender_en.delete(0, END)
        self.address_en.delete(0, END)
        self.dob_en.delete(0, END)

    def save(self):
        if self.name_en.get() == '' or self.psw_en.get() == '' or self.gender_en.get() == '' or \
                self.address_en.get() == '' or self.phone_en.get() == '' or self.uname_en.get() == '' or \
                self.mail_en.get() == '' or self.dob_en.get() == '':
            messagebox.showerror('error', 'please fill all the info')
        elif self.psw_en.get() != self.con_psw_en.get():
            messagebox.showerror('error', 'password does not match')
        else:
            name = self.name_en.get()
            psw = self.psw_en.get()
            gender = self.gender_en.get()
            address = self.address_en.get()
            phone = self.phone_en.get()
            user_name = self.uname_en.get()
            mail = self.mail_en.get()
            dob = self.dob_en.get()
            self.nam.savenew(name, psw, user_name, dob, gender, address, phone, mail)
            messagebox.showinfo('success','registration successfully')


def main():
    log = Tk()
    Reg(log)
    log.mainloop()


if __name__ == "__main__":
    main()
